#merge_sort :归并排序
n = int(input())
list_n = [int(x) for x in input().split()]
def merge_sort(list_n, l, r):
    if l >= r:
        return
    mid = l + r >> 1

    merge_sort(list_n, mid + 1, r)
    merge_sort(list_n, l, mid)

    tmp = list(range(r - l + 1))
    i, j, k = l, mid + 1, 0
    while i <= mid and j <= r:
        if list_n[i] < list_n[j]:
            tmp[k] = list_n[i]
            i += 1
        else:
            tmp[k] = list_n[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = list_n[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = list_n[j]
        j += 1
        k += 1
    list_n[l:r + 1] = [x for x in tmp]

merge_sort(list_n, 0, n - 1)
[print(x, end=' ') for x in list_n]

#reverse_pair_num
#在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
class Solution:
    def  merge(self,List,l,r)->int:
        if l>=r:
            return 0
        res=0
        mid = l+r>>1

        res+=self.merge(List,l,mid)
        res+=self.merge(List,mid+1,r)

        tmp=[0 for i in range(r-l+1)]

        i,j,k=l,mid+1,0
        while i<=mid and j<=r:
            if List[i]>List[j]:
                tmp[k]=List[j]
                j+=1
                res += (mid-i+1)
            else:
                tmp[k]=List[i]
                i+=1
            k+=1
        while i<=mid:
            tmp[k]=List[i]
            i+=1
            k+=1

        while j<=r:
            tmp[k]=List[j]
            j+=1
            k+=1

        List[l:r+1]=tmp
        return res

    def reversePairs(self, nums) -> int:
       return self.merge(nums,0,len(nums)-1)