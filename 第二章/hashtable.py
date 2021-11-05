#hash 1、拉链法

class hash1():

    N=10e6+3
    def __init__(self):
        self.h=[-1]*hash.N
        #值
        self.e=[None]*hash.N
        #下一个值位置
        self.ne=[None]*hash.N
        self.idx=0

        def insert(x):
            k=(x%hash.N+hash.N)%hash.N
            self.e[self.idx]=x
            self.ne[self.idx]=self.h[k]
            self.h[k]=self.idx
            self.idx+=1

        def find(x):
            k = (x % hash.N + hash.N) % hash.N

            i=self.h[k]
            while(i!=-1):
                if self.e[i]==x:
                    return True
                i=self.ne[i]

            return False

class hash2():#线性探测
    N = 2*10e6 + 3

    def __init__(self):
        self.h = [None] * hash.N

        def insert(x):
            pos=self.find(x)
            self.h[pos]=x

        def find(x): #如果有值返回对应位置 否则返回应该插入的位置
            k = (x % hash.N + hash.N) % hash.N

            while (self.h[k]!=None and self.h[k]!=x):
                k+=1
                if k==hash2.N: k=0
            return k