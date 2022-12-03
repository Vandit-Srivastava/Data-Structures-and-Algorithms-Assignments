######################################################################## max heap implementation begins ############################################################################################## 
class max_heap():
    def __init__(self):
        self.data=[]
    def swap(self,u1,u2,index):
        self.data[u1],self.data[u2]=self.data[u2],self.data[u1]
        index[self.data[u1]],index[self.data[u2]]=index[self.data[u2]],index[self.data[u1]]
    
    def heap_down(self,u,key,index):
        if 2*u+1<len(self.data):
            left=2*u+1
            swapper=left
            if 2*u+2<len(self.data):
                right=2*u+2
                if key[self.data[right]]>key[self.data[left]]:
                        swapper=right                    
            if key[self.data[swapper]]>key[self.data[u]]:
                self.swap(u,swapper,index)
                self.heap_down(swapper,key,index)
    
    def heap_up(self,u,key,index):
        if u>0:
            if key[self.data[u]]>key[self.data[(u-1)//2]]:
                self.swap(u,(u-1)//2,index)
                self.heap_up((u-1)//2,key,index)

    def extract_max(self,key,index):        #Deletes max, heapifies the list and returns the deleted max. O(log(m))
        self.swap(0,-1,index)
        max_cap_v=self.data.pop()
        self.heap_down(0,key,index)
        return max_cap_v

    def change_key(self,u,x,key,index):     #changes key and heapifies the list. O(log(m))
        x_old=key[self.data[u]]
        key[self.data[u]]=x
        if x>x_old:
            self.heap_up(u,key,index)
        else:
            self.heap_down(u,key,index)

    def heapify(self,key,index):
        for i in range(len(self.data)-1,-1,-1):
            self.heap_down(i,key,index)

######################################################################### max heap implementation ends ############################################################################################## 

def findMaxCapacity(n,links,s,t):
    #make graph adj list
    graph=[]
    for i in range(n):
        graph.append([])

    for e in links:
        graph[e[0]].append((e[1],e[2]))
        graph[e[1]].append((e[0],e[2]))

    cap=[0]*n
    cap[s]=float('inf')
    path=[None]*n
    path[s]=s

    heap=max_heap()
    index=[]
    for i in range(n):
        heap.data.append(i)
        index.append(i)
    heap.data[s],heap.data[0]=heap.data[0],heap.data[s]
    index[s],index[0]=index[0],index[s]
    while(len(heap.data)!=0):
        max_cap_v=heap.extract_max(cap,index)
        if max_cap_v==t:
            break
        for e in graph[max_cap_v]:
            cap_offered=min(cap[max_cap_v],e[1])
            if cap_offered>cap[e[0]]:
                heap.change_key(index[e[0]],cap_offered,cap,index)
                path[e[0]]=max_cap_v
    C=cap[t]
    backtrack=[t]
    cur=t
    while (cur!=s):
        cur=path[cur]
        backtrack.append(cur)
    r=len(backtrack)
    route=[None]*r
    for i in range(r):
        route[i]=backtrack[r-1-i]
    return (C,route)

################################################################################### input/output #####################################################################

#print(findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1))
#print(findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))
#print(findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3))
#print(findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2))
#print(findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5))