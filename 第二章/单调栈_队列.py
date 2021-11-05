#单调栈：常见模型：找出每个数左边离它最近的比它大/小的数
N=int(10e3)


def find_min_left(list_a,n):#找出每个数左边离它最近的比它小的数
    stack = [0] * N#如果 stack[i]>stack[j] and i<j
    tt = 0          #那么 由于stack[j]比较小 而且 距离 x更近，因此更本不会使用到stack[i](能用stack[i],那么一定能用到stack[j])
                    # 所以可以删除stack[i]
                    #因此单调
    for i in range(1,n+1):
        while tt>0 and stack[tt]>=list_a[i-1]:
            tt-=1#入栈前寻找<list_a[i]的值,删除掉stack[i]>list_a[i]的stack[i]

        if tt==0:#栈空
            print(-1,end=' ')
        else:   #栈非空
            print(stack[tt],end=' ')

        tt+=1   #入栈当前值
        stack[tt]=list_a[i-1]
#单调队列：找出滑动窗口最大值/最小值
def dandiao_duilie(list_a,k):#找到滑动窗口k内的最大值
    queue=[0]*100 #queue存的是下标
    hh=0
    tt=-1
    #如果队列中存储的 queue[i]<queue[j] and list_a[queue[i]]<list_a[queue[j]]
    #那么 滑动窗口中 queue[j]的值比queue[i]的值更大 而且 存的时间更久
    #因此 滑动窗口中最大值永远不会取到queue[i]，就删除queue[i]
    for i in range(len(list_a)):
        if(hh<=tt and i-k+1>queue[hh]):#如果队列里存的 下标不在滑动窗口中
            hh+=1
        while(hh<=tt and list_a[queue[tt]]<list_a[i]):#滑动窗口中存的是小值的下标,删除队列中的值
            tt-=1#把后面的值删除

        tt+=1
        queue[tt]=i
        if i>=k-1:
            print(list_a[queue[hh]],end=' ')







if __name__=='__main__':
    find_min_left([1,2,4,5,2,3,8,2],8)
    print()
    dandiao_duilie([1,2,4,5,2,3,8,2],3)