class tx_node():
    def __init__(self,point,parent=None):
        self.point=point
        self.left=None
        self.right=None
        self.parent=parent
        self.ty=None

class ty_node():
    def __init__(self,point,parent=None):
        self.point=point
        self.left=None
        self.right=None
        self.parent=parent

def make_ty(list,d0,d1):      #makes balanced bst out of a sorted list input for ty tree. note: d1 is not included d0 is included
    if d0>=d1:
        return None
    root_index=(d0+d1-1)//2
    node=ty_node(list[root_index])
    lc=make_ty(list,d0,root_index)
    rc=make_ty(list,root_index+1,d1)
    if lc!=None:
        lc.parent=node
    if rc!=None:
        rc.parent=node
    node.left=lc
    node.right=rc
    return node


def db_helper(list):                    #helper function for making pointdatabase
    if list==[]:
        return None
    
    ty=make_ty(list,0,len(list))
    if len(list)==1:
        node=tx_node(list[0])
        node.ty=ty
        return node

    #finding the x-median
    x_list=[]
    for i in range(len(list)):          #creates a copy of the list
        x_list.append(list[i])
    x_list.sort()
    x_med=x_list[(len(x_list)-1)//2]    #point tuple representing median
    
    left_list=[]
    right_list=[]
    for i in range(len(list)):
        if list[i][0]<x_med[0]:
            left_list.append(list[i])
        elif list[i][0]>x_med[0]:
            right_list.append(list[i])
    
    node=tx_node(x_med)
    node.ty=ty
    lc=db_helper(left_list)
    rc=db_helper(right_list)
    if lc!=None:
        lc.parent=node
    if rc!=None:
        rc.parent=node
    node.left=lc
    node.right=rc
    return node

def ty_point_appender(ty,list):
    if ty==None:
        return
    list.append(ty.point)
    ty_point_appender(ty.left,list)
    ty_point_appender(ty.right,list)

def search_ty(ty,y_int,list):
    v=ty
    while v!=None:
        if y_int[0]>v.point[1]:
            v=v.right
        elif y_int[1]<v.point[1]:
            v=v.left
        else:
            list.append(v.point)
            v1=v.left
            v2=v.right
            while v1!=None:
                if v1.point[1]>y_int[0]:
                    list.append(v1.point)
                    ty_point_appender(v1.right,list)
                    v1=v1.left
                else:
                    v1=v1.right
            while v2!=None:
                if v2.point[1]<y_int[1]:
                    list.append(v2.point)
                    ty_point_appender(v2.left,list)
                    v2=v2.right
                else:
                    v2=v2.left
            break
    

##################################################################### class implementation follows ##################################################################

class PointDatabase():
    def __init__(self, pointlist):
        pointlist.sort(key=lambda x : x[1])
        self.db=db_helper(pointlist)

    def searchNearby(self, q, d):
        list_nearby=[]
        x_int=(q[0]-d,q[0]+d)                  #2-D interval
        y_int=(q[1]-d,q[1]+d)
        v=self.db
        while v!=None:
            if x_int[0]>v.point[0]:
                v=v.right
            elif x_int[1]<v.point[0]:
                v=v.left
            else:
                if v.point[1]>y_int[0] and v.point[1]<y_int[1]:
                    list_nearby.append(v.point)
                v1=v.left
                v2=v.right
                while v1!=None:
                    if x_int[0]<v1.point[0]:
                        if v1.point[1]>y_int[0] and v1.point[1]<y_int[1]:
                            list_nearby.append(v1.point)
                        if v1.right!=None:
                            search_ty(v1.right.ty,y_int,list_nearby)
                        v1=v1.left
                    else:
                        v1=v1.right
                while v2!=None:
                    if x_int[1]>v2.point[0]:
                        if v2.point[1]>y_int[0] and v2.point[1]<y_int[1]:
                            list_nearby.append(v2.point)
                        if v2.left!=None:
                            search_ty(v2.left.ty,y_int,list_nearby)
                        v2=v2.right
                    else:
                        v2=v2.left
                break
        return list_nearby

######################################################################################################################################################################
