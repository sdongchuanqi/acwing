

#算法思想：可以看作一个n个决策序列
# 第1步把 两个n放到可选的对应的位置    即下标i,j 其中j等于i+n+1
# 第k步把 两个n-k+1的数放到合适的位置 即下标i，j 其中j等于i+n-k+2
#   每次从i从0开始寻找到两个间隔为n-k+2的空位，把两个相同的数同时放到该位置
#题目1
def magic1(n):
    A=[0]*2*n               #存放神奇数组元素
    used=[False]*2*n        #标记位置是否可用
    def backtracing(step):
        if step==0:         #结束决策序列
            for i in range(2*n):
                if used[i]==False:          #判断是否把所有数放入
                    return 0 #返回递归调用次数
            print(A)         #打印结果

            return 0    #返回递归调用次数

        cnt=0
        for j in range(2*n):
            # 如果存在间隔为step+1的空位就连续放入两个数
            if used[j]==False and j+step+1<2*n and used[j+step+1]==False:
                #放数，标记使用
                used[j]=True
                used[j+step+1]=True
                A[j]=step
                A[j+step+1]=step

                cnt+=backtracing(step-1)
                #记录调用次数
                cnt+=1

                #回溯
                used[j]=False
                used[j+step+1]=False
        return cnt

    return backtracing(n)

def magic2(n):
    A = [0] * 2 * n                             #存放神奇数组元素
    used = [False] * 2 * n                      #标记位置是否可用
    def backtracing(step):
        if step == 0:                        #结束决策序列
            for i in range(2 * n):
                if used[i] == False:          #判断是否把所有数放入
                    return 0,False          #返回调用次数，未找到合法序列
            print(A)                        #打印结果
            return 0,True                   #返回调用次数，找到合法序列
        cnt = 0
        for j in range(2 * n):
            # 如果存在间隔为step+1的空位就连续放入两个数
            if used[j] == False and j + step + 1 < 2 * n and used[j + step + 1] == False:
                used[j] = True            #放数，标记使用
                used[j + step + 1] = True
                A[j] = step
                A[j + step + 1] = step
                tmp,find= backtracing(step - 1)
                if find:                            #找到结果，直接返回到根节点
                    return cnt+1+tmp,True

                cnt += (1+tmp)                  #记录调用次数
                used[j] = False                 #回溯
                used[j + step + 1] = False

        return cnt,False                        #如果都没找到，就返回不存在合法序列
    return backtracing(n)

#题目2
# 算法思想：可以看作一个n个决策序列
# 第i步决定把S[i]的数放到k个子集和的某个子集去
#   在假定S多重集合的元素都是大于等于零的情况下，剪枝掉那些子集和大于sum(S)//k的树枝
#
def divide_S(S, k):
    if sum(S) // k * k != sum(S):       #S的和能整除k？不能就直接返回
        return
    else:
        target = sum(S) // k            #记录每个子集的和

    n = len(S)
    divide = []
    for i in range(k):                  #初始化K个空子集
        divide.append([])

    def backtracing(i):
        if i >= n:
            for i in range(k):          #判断每个子集和是否是target
                if sum(divide[i]) != target:
                    return  # 失败返回
            for i in range(k):          #输出出结果
                print(divide[i],end='  ')
            print()

            return

        for j in range(k):              #进行k种决策 把S[i]放到第j个子集中去
            if sum(divide[j]) + S[i] <= target:     # 在假定S的所有元素都大于0的情况下 进行剪枝子集和大于target的值，否则不能进行剪枝
                divide[j].append(S[i])  #放入
                backtracing(i + 1)
                divide[j].pop(-1)       #回溯
    backtracing(0)

if __name__=='__main__':
    print('n=4的全部的调用次数:',magic1(4))
    print('n=31找到一个的调用次数:',magic2(31)[0])
    S=[7,3,5,12,2,1,5,3,8,4,6,4]
    divide_S(S,2)