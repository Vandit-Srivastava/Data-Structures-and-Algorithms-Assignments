class stack():  #implementing the class "stack"
    DefaultSize=10
    def __init__(self):
        '''Creates an empty stack, a list of size=Default size'''
        self.data=[None]*self.DefaultSize
        self.size=0

    def push(self,e):
        '''Pushes element e to the top of the stack'''
        if self.data[-1]!=None:
            old=self.data
            self.data=[None]*(2*self.size)
            for i in range(self.size):
                self.data[i]=old[i]
        self.data[self.size]=e
        self.size+=1

    def pop(self):
        '''Removes top element from stack. If stack is empty,raise empty exception'''
        if self.size==0:
            raise Exception('stack is empty')
        a=self.data[self.size-1]
        self.data[self.size-1]=None
        self.size-=1
        return a
    
    def top(self):
        '''Returns top element from stack. If stack is empty,raise empty exception'''
        if self.size==0:
            raise Exception('stack is empty')
        return self.data[self.size-1]

    def len(self):
        '''Returns length of the stack'''
        return(self.size)

    def Is_Empty(self):
        '''Returns true is stack is empty else false.'''
        if self.size==0:
            return True
        return False

def stacker(P):
    '''converts input string into stack'''
    prog=stack()                                #Program for drone represented as a stack
    for i in range(len(P)):
        prog.push(P[i])
    return prog

def reader(prog):                               #Read the stack and implement the program conveyed by it
    list=[0,0,0,0]
    while prog.size!=0:
        a=prog.pop()
        if a=="X":
            if prog.pop()=="+":
                list[0]+=1
                list[3]+=1
            else:
                list[0]-=1
                list[3]+=1

        elif a=="Y":
            if prog.pop()=="+":
                list[1]+=1
                list[3]+=1
            else:
                list[1]-=1
                list[3]+=1

        elif a=="Z":
            if prog.pop()=="+":
                list[2]+=1
                list[3]+=1
            else:
                list[2]-=1
                list[3]+=1            

        elif a==")":
            l=reader(prog)
            f=0
            i=0
            while prog.size!=0:
                if prog.top() not in ["X","Y","Z","+","-","(",")"]:
                    f+=int(prog.pop())*(10**i)
                    i+=1
                else:
                    break
            list[0]=list[0]+l[0]*f
            list[1]=list[1]+l[1]*f
            list[2]=list[2]+l[2]*f
            list[3]=list[3]+l[3]*f
        
        elif a=="(":
            return list
    return list 


def findPositionandDistance(P):
    prog=stacker(P)
    return reader(prog)
