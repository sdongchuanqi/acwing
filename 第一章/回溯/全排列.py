#步骤

"""
一条路径可以看作一条决策序列
	第i步决定候选方案

A=[None]*(n+1)
Used=[False]*(n+1)

全排列
def backtracing(i):
	if (i>n):
		print(A)
	else:
		for c in range(1,n+1):
			if (used[c]==False):
				A[i]=c
				used[c]=True
				backtracing(i+1)
				used[c]=False
	return

#生成简单路径  s->t
结束条件 没有可选路径
i->[1->|path|+1]



path={node:[node1,node2,node3]}
def generate_path(i)
	if i==1:
		used[s]=True
		A[i]=s
		generate_path(i+1)
	else:
		if A[i-1]==t:
			print(A[1:i])
		else:
			for c in path[A[i-1]]:
				if used[c]==False:
					used[c]=True
					A[i]=c
					generate_path(i+1)
					used[c]=False
	return

n皇后

used=[False]*(n+1)

def queen(i):
	if i>n:
		print(A)
		return

	for c in range(1,n+1):
		label=True
		for j in range(1,i):
			if A[j]==c or abs(A[j]-c)==abs(j-i):
				label=False
				#continue
		if label:
			A[i]=c
			queen(i+1)


子集和
长度不超过n的决策序列
第1步、X[1..n]中是否存在子集，和为t
第i步、X[i..n]中是否存在子集,和为d
	决定是否放入Y中，决策方案：只有两种，与之前决策无关
		1、放 x[i+1..n]是否存在子集，和为d-X[i]
		2、不放x[i+1..n]是否存在子集，和为d
	A[1..i-1]是否是一个解
	d=0:是一个解，因为空集是A[i..n]的一个子集
	d<0:不是
	d>0:
		1、i>n 不是一个解
		2、否则，考虑是否将元素X[i]放入子集Y




def generate_subset_sum(i,d):
	if d==0:
		print(A[1:i])
	elif d>0:
		if i<=n:
			for c in range(2):
				A[i]=c
				if c==0:
					generate_subset_sum(i+1,d)
				else:
					generate_subset_sum(i+1,d-X[i])

X=[None,8,6,4,7,]
t=15
A=[None]*(len(X))
n=len(X)-1

generate_subset_sum(1,t)



文本分割
给定一串字符，能够分割成若干单词

sub_fun :is_word(w)
	:arg  w：字串
	:return if w是单词 返回True,else False

split = []

第i步：最多n步
def gene_segment(i):
	if A[i-1]==n:
		print(A)
	else:
		for c in range(A[i-1]+1,n+1):
			if is_word(S[A[i-1]+1:c+1]):
				A[i]=c
				gene_segment(i+1）

s=' sadasda'
n=len(n)-1
A=[0]*n
gene_segment(1)



i是下标
def subword(i):
	if i>n:
		if split[-1]==n:
			print(split.copy())
		return

	for j in range(i,n+1):
		if is_subword(S[i:j]):
			split.append(j-1)
			subword(j)
			split.pop(-1)






最长递增子序列：子序列：可以删除 回溯法：
长度为n的决策序列:
	第i步时决定是否将元素i放入子序列：
	不放a[i]=0
	放：a[i]=1：如果放则需要条件：大于最后一个元素，同时更新最大值 x[i]>t：t=x[i]
	结束条件：i>n

def generate_lst(i,t,l):
	global m     #:max length of subseq
	if i>n:
		if l>m:#find a new seq
			sol.clear()
			sol.add(tuple(A[1:]))
			m=l
		elif l==m:
			aol.add(tuple(A[1:]))
	else；
		for c i in range(2):
			if c==0:
				A[i]=0
				generate_lst(i+1,t,l)
			else:
			if A[i]>t:
				A[i]=1
				generate_lst(i+1,x[i],l+1)
x=[None,2,3,4,2,3]
sol=set()
A=[N]*len(x)
m=0
动态规划：每次决定选择放入的下标是大于x[i]的最小下标，使用二分查找                单调栈
def LIS(lst):
	n=len(lst)
	idx=-1
	dp=[0]*n
	for i in range(n):
		if idx<0 or dp[idx]<lst[i]:
			idx+=1
			dp[idx]=lst{i]
		else:
			pos=bin_search(dp[0:idx+1],x[i])		#在dp中 找到大于等于x[i]的最小元素下标
			dp[pos]=x[i]
	return idx+1



最优二叉搜索树：

看作一个长度为n的决策序列：
第1步 从[1:N]中选择根结点
	第i步 从V[i..j]选出第k个作为根节点

def generate_bst(low,high):#得到所有二叉搜索树
	if low>high:
		return [[]]
	elif low==high:
		[[low]]
	else:
		bst=[]
		for c in range(low,high+1):
			L=generate_bst(low,c-1)
			R=generate_bst(c+1,high)
			ts=[[c,l,r] for l in L for r in R]
			bst.extend(ts)
		return bst



def Optim_search_tree(V):

	n=len(V)
	if n==0:
		return 0,None

	best_root=0
	best_value=0
	b_l=[]
	r_l=[]

	tree=[]

	for i in range(n):
		left,l_tree=Optim_search_tree(V[1:i])
		right,r_tree=Optim_search_tree(V[i+1:n])
		all_vaue=left+right+sum(V)
		if best_value<all_value:
			best_value=all_value
			best_root=i
			b_l=l_tree
			r_l=r_tree
	tree.extend([best_root,b_l,r_l])
	return best_value,tree

"""

n=4

used=[False]*(n+1)
res=[]


def backtracing(i,A):
	if (i>n):
		res.append(A.copy())
		return 
	else:
		for c in range(1,n+1):
			if (used[c]==False):
				used[c]=True
				A.append(c)
				backtracing(i+1,A)

				used[c]=False
				A.pop(-1)		
	return 
backtracing(1,[])
print(res)
