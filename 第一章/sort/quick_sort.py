n = int(input())
list_n = input()
list_n = [int(x) for x in list_n.split()]
#1快排 严蔚敏 版
#要点  partition
#    1、区间：[low,high]
#    2、循环结束：i=j=position
#   quick_sort:每次都会确定一个位置
def partition(list_n,low,high):
    spot = list_n[low] #把low值存到spot
    while low<high:
        while low<high and list_n[high]>=spot:
            high-=1
        list_n[low]=list_n[high]
        while low<high and list_n[low]<spot:
            low+=1
        list_n[high]=list_n[low]
    list_n[high]=spot
    return high
def qick_sort(list_n, low, high):
    if low<high:
        position = partition(list_n,low,high)
        qick_sort(list_n, low, position-1)
        qick_sort(list_n, position+1, high)
    return
#2 、 accept——quick_sort: 模板快排
def quick_sort(list_n, l, r):
    if l >= r:
        return
    #i和j分别取的是列表外的边界，因为做的是do i++ while list[i]<x 的循环，基于 每次 交换后 都先加1的假设 而做 而且    取中间值的作用是 避免边界死递归
    i, j, x = l - 1, r + 1, list_n[l + r >> 1]
    #把划分为<=x和>=x的两部分、但是do while 循环里的是不带等号的判断
    #前半部分找到 >=x 的i ，后半部分找到<=x的j  if i<j swap
    #按照[l,j] ,[j+1,r]划分是因为j的后面保证了<=x,
    #类似的可以按照 [l,i-1],[i,r]划分，i-1保证了>=x
    while i < j:
        while True:
            i += 1
            if list_n[i] >= x:
                break
        while True:
            j -= 1
            if list_n[j] <= x:
                break
        if i < j:
            tmp = list_n[j]
            list_n[j] = list_n[i]
            list_n[i] = tmp
    quick_sort(list_n, l, j)
    quick_sort(list_n, j + 1, r)
qick_sort(list_n, 0, n-1)
print(list_n)

#给定一个长度为 n 的整数数列，以及一个整数 k，请用快速选择算法求出数列从小到大排序后的第 k 个数。
n_k = [int(x) for x in input().split()]
n, k = n_k[0], n_k[1]
list_n = [int(x) for x in input().split()]
def k_th(list_n, l, r, k):
    if l == r:
        return list_n[l]
    # print(list_n,k)
    i, j, x = l - 1, r + 1, list_n[l + r >> 1]

    while i < j:
        while True:
            i += 1
            if list_n[i] >= x:
                break
        while True:
            j -= 1
            if list_n[j] <= x:
                break

        if i < j:
            tmp = list_n[i]
            list_n[i] = list_n[j]
            list_n[j] = tmp

    if j < k - 1:
        return k_th(list_n, j + 1, r, k)
    else:
        return k_th(list_n, l, j, k)
print(k_th(list_n, 0, n - 1, k))

