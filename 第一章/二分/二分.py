#整数二分：二分的本质：给定一个区间，区间[l,r]上存在某种性质，使得性质在给定的某个边界l<=x<=r左边满足，而在该边界x的右边不满足。
#                 那么就可以使用二分进行查找边界x
#两个模板 分别对应二分边界 满足性质x的边界X 和 不满足该性质x的边界Y(设为满足性质y的边界)   [xxxxxxxX Yyyyyyyyy]
# #1、 寻找满足性质x的边界X ：mid = (l+r+1)/2 if (check_x(mid)) true:[mid,r] 更新 l=mid    false:[l,mid-1] 更新 r=mid-1
#区间划分为 [l,mid-1] , [mid,r]

def  sort_1(l,r):
    def check(mid):
        return True


    mid = l+r+1>1
    while (l<r):
        if check(mid):
            l=mid
        else:
            r=mid-1
    return r


#2、 寻找满足性质y的边界Y ：mid = (l+r)/2 if (check_y(mid)) true:[l,mid] 更新 r=mid    false:[mid+1,r] 更新 l=mid+1

def sort_2(l,r):
    def check(mid):
        return True

    mid = l+r
    while (l<r):
        if check(mid):
            r=mid
        else:
            l=mid+1

    return r
#789. 数的范围给定一个按照升序排列的长度为 n 的整数数组，以及 q 个查询。

#对于每个查询，返回一个元素 k 的起始位置和终止位置（位置从 0 开始计数）。

#如果数组中不存在该元素，则返回 -1 -1。

def sort():
    n,q=(int(x) for x in input().split())
    list_n = [int(x) for x in input().split()]
    q_list = []
    for i in range(q):
        q_list.append(int(input()))

    k = 0
    while (k < q):
        x = q_list[k]
        k += 1

        l, r = 0, n - 1
        while (l < r):
            mid = l + r >> 1
            if (list_n[mid] >= x):
                r = mid
            else:
                l = mid + 1
        if (list_n[r] != x):
            print("-1 -1")
            continue

        low = l
        l, r = l, n - 1
        while (l < r):
            mid = l + r + 1 >> 1
            if (list_n[mid] == x):
                l = mid
            else:
                r = mid - 1

        print(str(low) + ' ' + str(r))




