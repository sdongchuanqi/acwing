#手写一个堆操作
#1、如何插入一个数  ：size++;heap[size]=x up(size)
#2、集合的最小值：heap[1]
#3、删除最小值：heap[1]=heap[size];size--;down(1)
#4、删除任意一个元素 ：heap[k]=heap[size];size--;down[k];up(k)
#5、修改任意一个元素 heap[k]=x;down(k);up(k)

class heap():
    N=10e6+10#类变量
    def __init__(self,list_a):
        self.h=[0]*heap.N
        self.size=0

        for i in list_a:#读入heap
            self.size+=1
            self.h[self.size]=i

        for i in range(self.size//2,0,-1):# 初始化一个堆
            self.down(i)

    def down(self,k):
        '''
        tmp=self.h[k]
        while (2*k<=self.size):
            t=2*k
            if (t+1<=self.size and self.h[t+1]<self.h[t]):
                t+=1
            if self.h[t]<tmp:#小的向上移动
                self.h[k]=self.h[t]
                k=t
            else:
                break
        self.h[k]=tmp

        :param k:
        :return:
        '''
        u=k
        if k*2<=self.size and self.h[k*2]<self.h[u]:
            u=k*2
        if k*2+1<=self.size and self.h[k*2+1]<self.h[u]:
            u=k*2+1
        if u!=k:
            tmp=self.h[k]
            self.h[k]=self.h[u]
            self.h[u]=tmp

            self.down(u)
    def up(self,k):

        '''
        u=k
        while(u>=1 and self.h[u//2]>self.h[u]):
            swap(self.h[u//2],self.h[u])
            u=u//2

        :param k:
        :return:
        '''
        u=k
        if k//2>=1 and self.h[k//2]<self.h[k]:
            u=k//2
        if k!=u:
            tmp=self.h[k]
            self.h[k]=self.h[u]
            self.h[u]=tmp

            self.up(u)




