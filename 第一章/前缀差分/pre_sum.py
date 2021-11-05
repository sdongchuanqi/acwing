#前缀和
#设A的元素下标为1，n
#A[0]=0
##s[0]=0
# for i in range(1,n+1):
#       s[i]=s[i-1]+A[i]

#作用 :求[l,r]的和 1<=l<=r<=n 在O(1)的时间复杂度中 s[r] -s[l-1] 求[l,r]
def pre_sum(A):
    #A :[0]+A
    A= [0]+A
    S=[0]
    for i in range(1,len(A)):
        S.append(S[i-1]+A[i])
    return S
print(pre_sum([1,2,3,4]))

def l_r_sum_A(A,l,r):
    S=pre_sum(A)
    return S[r+1]-S[l] #计算A中前r个数的和 减去前l-1个数的和 得到最终的和
print(l_r_sum_A([1,2,3,4],0,2))

#二维的前缀和
#求和 S[i][j] = S[i-1][j]+S[i][j-1] -S[i-1][j-1]+A[i][J]
#求值 [x_l,y_l]---[x_r,y_r]   sum=S[x_r,y_r] - S[x_l-1,y_r]-S[x_r,y_l-1]+S[x_l-1,y_l-1]

#差分：给A的[l,r]这个区间中的每个数加上c:
# 基础操作B[l]+=c B[r+1]-=c 然后使用O(n)的时间对B求前缀和的到A
#构建差分数组：A=全零 然后把B[i,i]都加上A[i]

#二维差分：S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c