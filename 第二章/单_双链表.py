N=10e7
class single_link():
    def __init__(self):
        self.head=-1
        self.idx=0
        self.e=[0]*N
        self.ne=[0]*N

    def insert(self,a):#链表头插入一个数a
        self.e[self.idx]=a
        self.ne[self.idx]=self.head
        self.head=self.idx
        self.idx+=1

    #删除头节点
    def remove(self):
        self.head=self.ne[self.head]


class double_link():
    def __init__(self):
        self.e=[0]*N
        self.l=[0]*N
        self.r=[0]*N
        '''
        e[]表示节点的值，l[]表示节点的左指针，r[]表示节点的右指针，
        idx表示当前用到了哪个节点'''
        self.r[0]=1#0是左端点，1是右端点
        self.l[1]=0
        self.idx=2
    def insert(self,a,x):#在节点a的右边插入一个数x
        self.e[self.idx]=x
        #指向别人
        self.l[self.idx]=a
        self.r[self.idx]=self.r[a]
        #别人指向自己
        self.l[self.r[a]]=self.idx
        self.r[self.l[a]]=self.idx
        self.idx+=1

    def remove(self,a):
        self.l[self.r[a]]=self.l[a]
        self.r[self.l[a]]=self.r[a]

class stack():
    def __init__(self):
        self.stack=[0]*N
        self.tt=0

    def insert(self,x):
        self.tt+=1
        self.stack[self.tt] = x

    def remove(self):
        self.tt-=1

    def get(self):
        return self.stack[self.tt]

    def empty(self):
        return self.tt<=0

class queue():
    def __init__(self):
        #hh 表示队头，tt表示队尾
        self.q=[0]*N
        self.hh=0
        self.tt=-1
    def insert(self,x):
        self.tt+=1
        self.q[self.tt]=x
    def get(self):
        return self.q[self.hh]

    def empty(self):
        return self.hh>self.tt

class circle_queue():
    def __init__(self):
        self.q=[0]*N
        self.hh=0
        self.tt=0

    def insert(self,x):

        self.q[self.tt]=x
        self.tt+=1
        if self.tt==N:
            self.tt=0

    def remove(self):
        self.hh+=1

        if self.hh==N:
            self.hh==0

    def get(self):
        return self.q[self.hh]

    def empty(self):
        return self.hh==self.tt


