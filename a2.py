class min_heap():
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
                if key[self.data[right]]!=None:
                    if key[self.data[left]]==None:
                        swapper=right
                    elif key[self.data[right]]<key[self.data[left]] or (key[self.data[right]]==key[self.data[left]] and self.data[right]<self.data[left]):
                        swapper=right
            if key[self.data[swapper]]!=None:
                if key[self.data[u]]==None:
                    self.swap(u,swapper,index)
                    self.heap_down(swapper,key,index)                    
                elif key[self.data[swapper]]<key[self.data[u]] or (key[self.data[swapper]]==key[self.data[u]] and self.data[swapper]<self.data[u]):
                    self.swap(u,swapper,index)
                    self.heap_down(swapper,key,index)
    
    def heap_up(self,u,key,index):
        if u>0:
            if key[self.data[u]]!=None:
                if key[self.data[(u-1)//2]]==None:
                    self.swap(u,(u-1)//2,index)
                    self.heap_up((u-1)//2,key,index)
                elif key[self.data[u]]<key[self.data[(u-1)//2]] or (key[self.data[u]]==key[self.data[(u-1)//2]] and self.data[u]<self.data[(u-1)//2]):
                    self.swap(u,(u-1)//2,index)
                    self.heap_up((u-1)//2,key,index)        

    def heapify(self,key,index):
        for i in range(len(self.data)-1,-1,-1):
            self.heap_down(i,key,index)

################################################################//end of min_heap implementation//##############################################


def listCollisions(M,x,v,m,T):
    n=len(M)
    if n<2:
        return []
    time=0
    t0=[0]*n

    col_time=[None]*(n-1)
    for i in range(n-1):
        if v[i]>v[i+1]:
            col_time[i]=(x[i+1]-x[i])/(v[i]-v[i+1])

    col_heap=min_heap()
    for i in range(n-1):
        col_heap.data.append(i)

    col_heap_index=[]
    for i in range(n-1):
        col_heap_index.append(i)

    col_heap.heapify(col_time,col_heap_index)       #builds col_heap and updates col_heap_index
    list=[]
    for c in range(m):
        if col_time[col_heap.data[0]]==None:
            break
        elif col_time[col_heap.data[0]]>T:
            break
        else:
            i=col_heap.data[0]
            time=(x[i+1]-x[i]+v[i]*t0[i]-v[i+1]*t0[i+1])/(v[i]-v[i+1])
            pos=(x[i+1]*v[i]-x[i]*v[i+1]+v[i]*v[i+1]*(t0[i]-t0[i+1]))/(v[i]-v[i+1])
            list.append((round(time,4),i,round(pos,4)))
            
            x[i]=pos
            x[i+1]=pos
            
            t0[i]=time
            t0[i+1]=time
            
            v1=((M[i]-M[i+1])*v[i]+2*M[i+1]*v[i+1])/(M[i]+M[i+1])
            v2=(2*M[i]*v[i]+(M[i+1]-M[i])*v[i+1])/(M[i]+M[i+1])
            v[i]=v1
            v[i+1]=v2

            col_time[i]=None
            col_heap.heap_down(0,col_time,col_heap_index)
            if i>0:
                if v[i-1]>v[i]:
                    col_time[i-1]=(x[i]-x[i-1]+v[i-1]*t0[i-1]-v[i]*t0[i])/(v[i-1]-v[i])
                else:
                    col_time[i-1]=None
                col_heap.heap_up(col_heap_index[i-1],col_time,col_heap_index)       #since after collisioin, i gains velocity backwards
            if i<n-2:
                if v[i+1]>v[i+2]:
                    col_time[i+1]=(x[i+2]-x[i+1]+v[i+1]*t0[i+1]-v[i+2]*t0[i+2])/(v[i+1]-v[i+2])
                else:
                    col_time[i+1]=None
                col_heap.heap_up(col_heap_index[i+1],col_time,col_heap_index)       #since after collision, i+1 gains velocity forwards
            
    return list

############################################################################################################################################################
