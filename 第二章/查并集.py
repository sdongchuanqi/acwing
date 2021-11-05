N=int(10e6+10)

p=[0]*N #记录其父节点的下标


#1、查询是否是一个根节点：p[x]==x
#2、查询两个集合是否同一个 find(a)==find(b)
#3、如何合并两个集合 ：p[find(a)]=p[find(b)]
#4、find 实现方法
#def find(x):
#   if(p[x]!=x):
#       p[x]=find(p[x])     #递归验证父节点是否是根节点， 并且让当前节点的节点指向根结点 ，（递归表示处理该路径上的所有节点）
#   return p[x]             #返回根节点
#

#查并集：
def find(x):#查根节点 + 路径压缩
    if p[x]!=x:     #根节点 p[x]=x
        p[x]=find(p[x])   #如果不是根节点就向父节点查找  路径压缩：：把所有从x到根结点路径上的所有的点  都（递归处理） 指向 根结点
    return p[x]        #返回最后的根结点


#1、M:合并两个并集   Q：查询两个节点是否在同一个集合内
def deal_merge():
    in_list = [int(x) for x in input().split()]
    n,m=in_list[0],in_list[1]#n:数自个数 m:操作个数

    for i in range(1,n+1):#初始化
        p[i]=i
    while m>0:
        op_list=input().split()
        op=op_list[0]
        a,b=int(op_list[1]),int(op_list[2])
        if op=='M':#合并两个集合 包括find(a)=find(b)的情况
            p[find(a)]=find(b)
        else:   #查询两个集和是否是同一个
            if find(a)==find(b):
                print('yes')
            else:
                print('false')
        m-=1
        print(p[0:13])
size=[0]*N
def deal_merge_with_size():#维护根节点size的查并集
    in_list = [int(x) for x in input().split()]
    n, m = in_list[0], in_list[1]  # n:数自个数 m:操作个数

    for i in range(1, n + 1):  # 初始化
        p[i] = i
        size[i]=1

    while m > 0:
        op_list = input().split()
        op = op_list[0]
        a, b = int(op_list[1]), int(op_list[2])

        if op == 'M':  # 合并两个集合 包括find(a)=find(b)的情况
            if find(a)!=find(b):
                size[find(b)]+=size[find(a)] #更新根节点的size
            p[find(a)] = find(b)             #归并两个节点所在的集合

        else:  # 查询两个集和是否是同一个
            if find(a) == find(b):
                print('yes')
                print(size[find(b)])
            else:
                print('false')

        m -= 1
        print(p[0:13])

if __name__=='__main__':
    '''
    12 3
    M 2 3
    M 2 7
    Q 3 7
    '''
    deal_merge_with_size()
    #deal_merge()






