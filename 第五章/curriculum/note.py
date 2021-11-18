#Fibonacci 记忆化搜索
N=10e6
F=[None]*int(N)
F[0]=0
F[1]=1
def memo_fibo(n):
    if F[n]==None:
        F[n]=memo_fibo(n-1)+memo_fibo(n-2)
    return F[n]

def iter_fibo(n):
    F[0]=0
    F[1]=1
    for i in range(2,n):
        F[i]=F[i-1]+F[i-2]
    return F[n]
#空间换时间

def iter_fibo_two(n):
    pre=0
    cur=1
    for i in range(2,n):
        next=cur+pre
        pre=cur
        cur=next
    return cur

#二项式系     C(n,k)=C(n-1,k-1)+C(n-1,k)
def Con(n,k):
    if k==0:
        return 1
    elif n==k:
        return 1
    elif k>n:
        return 0
    else:
        return Con(n-1,k-1)+Con(n-1,k)
def Con_dp(n,k):
    #设为None 更好调试程序
    dp=[[None]*(k+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0]=1

    for j in range(1,k+1):
        dp[j][j]=1

    for j in range(1,k+1):#从左向右 从上到下 行优先 或者 列优先都行
        for i in range(j+1,n+1):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    return dp[i][j]

#加权任务调度 开始时间s_i 结束时间e_i 权重w  找到一个最大权重的互不相交的任务子集
#1、按照结束时间排序
#


#2、定义一个在任务j之前完成 且 于任务j不相交的最大任务i P[j]=i   logn
#


# def Findsolution
#   if j==0:
#       return 空集
#   elif:
#       w_j+M[p[j]]>M[j-1]
#       return {j}UFindsolution(p[j])
#   else
#       return Findsolution(j-1)

#二元选择法构造递归：选着一个元素在集合里或则不在集合里
#1、任务包含任务n       opt(P[n])+w_n
#2、任务不包含任务n      opt(n-1)
#3、集合的属性求最大值

#多元选择构造递归：
#分割字符串
#
#splitable(n)={True                n==0
#          V(is_word(j,n) and splitable(j-1))

s=' 12342452343'
n=len(s)-1
M=[False]*(n+1)
def is_word(str):
    '''
    to be writed
    :param str:
    :return:
    '''
    return True
def splitable(n):
    M[0]=True
    for i in range(1,n+1):
        for  j in range(1,i+1):
            if is_word(s[j:i+1]) and M[j-1]:
                M[i]=True
                break
    return M[n]
def find_solu(j):
    if M[j]:
        for i in range(j-1,-1,-1):
            if M[i] and is_word(s[i+1:j+1]):
                return find_solu(i)+[s[i+1:j+1]]
    return []

#涂房子 相邻的两个的结果不相同 vibite 剪枝算法
#最小化费用

#cost[[]*3 for i in range(n)]
w=[[1,23,3],[3,5,4],[3,43,32]]
def pinter(n):
    pre=[0]*3
    cur=[0]*3
    for i in range(n):
        for j in range(3):
            cur[j]=0
            for k in range(3):
                if k!=j:
                    cur[j]=max(pre[k],cur[j])
            cur[j]+=w[i][j]
        pre=cur
        cur=[0]*3
    return pre

#使用二元选择选择关系 构造递归关系
# 给定整数序列 S[1..n] 最长递增子序列 O_n 长度 OPT(n)

#对于O_n 以下两种必定有一个成立
#   O_n 不包含 S[n] OPT(n) = OPT(n-1)
#   O_n 包含  S[n] OPT(n) ??? OPT(i)
    #但是 以上 仅使用一个变量 不容易刻画 关系
#S[1..n] i<j OPT(i,j)是 j..n 中满足 S[j..n]的子序列，且值都大于s[i]  (记录当前子序列的 最大数值)
#s[0] = -1e9
#j>n OPT(i,j)=0
#
#   s[i]>=s[j]   S[j] 不满住加入子序列的条件  OPT(i,j)=OPT(i,j+1)
#   s[i]<s[j]    S[j] 满足  OPT(i,j) = max(OPT(j,j+1)+1 ,OPT(i,j+1))
M = [[None] *(n+2) for _ in range(n+2)]
def OPT():
    for i in range(n+2):
        M[i][n+1]=0
    for j in range(n,0,-1):
        for i in range(j+1):
            if s[i]<s[j]:
                s[j] = max(M[i][j+1],M[j,j+1]+1)
            else:
                s[j] = M[i][j+1]
    return  M[0][1]

def find_sol(i,j):
    if j>n:
        return []
    if s[i]<s[j]:
        if M[i][j]==M[j][j+1]+1:
            return [s[j] + find_sol(j,j+1)]
        else:#skip s[j]
            return  find_sol(i, j + 1)
    else:    #skip s[j]
        return find_sol(i,j+1)


#使用多元选择关系 构造递归关系
#给定 整数序列 s[1..n] 令OPT(i) 是S[i..n]中满足以下条件 的递增子序列 其中治虚劳必须以  s[i]开始
#
#OPT[i] max( OPT[j]+1 for j in range(i+1,n) if s[j]>s[i],1)
M2=[1 *(n+1)]
def OPT2():
    for i in range(n-1,-1,-1):
        for j in range(i+1,n+1):
            if s[i]<s[j]:
                M2[i]=max(M2[i],1+M2[j])
    return M[0]-1

if __name__=='__main__':
    print(pinter(3))
