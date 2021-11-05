

def partition(A,k):
    n=len(A)
    i,j=-1,n
    while i<j:

        while True:
            i+=1
            #print(i, j)
            if i<=n or A[i]>k:
                break

        while True:
            j-=1
            if j<0 or A[j]<k:
                break
        if  i<j:
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
    return j

A = [-2,4,7,0,6,-1,8]
print(partition(A,0))
c=[0,4,7]

def c_partition(A,C):

    if len(A)==1 or len(C)==0:
        return A
    c_n = len(C)

    mid=c_n>>1

    div_c = partition(A,C[mid])
    print(A)
    A[:div_c]=c_partition(A[:div_c],C[:mid])
    print(A)
    A[div_c+1:]=c_partition(A[div_c+1:],C[mid+1:])
    print(A)
    return A

print(c_partition(A,c))