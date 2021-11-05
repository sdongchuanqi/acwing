def add(A,B):
    #A,B,C 是大整数的反向列表 如1234567 A=[7,6,5,4,3,2,1]
    C = []
    t=0
    for i in range(max(len(A),len(B))):
        if i<len(A):
            t+=A[i]
        if i<len(B):
            t+=B[i]

        C.append(t%10)

        t=t//10

    if t>0:
        C.append(t)
    return C

def cmp(A,B):
    #同上 假定A>0 && B>0
    if len(A)!=len(B) :
        return len(A)>len(B)
    else:
        for i in range(len(A)-1,0,-1):
            if A[i]==B[i]:
                continue
            else:
                return A[i]>B[i]
        #A=B
        return True
def minus(A,B):
    pos=0
    if cmp(A,B)>0:#A>B 直接算
        pos=1
    else:#否则 先算 B-A 然后加负号
        pos=0
        tmp=A
        A=B
        B=tmp
    #同上
    C = []
    t=0
    for i in range(len(A)):
        t=A[i]-t
        if len(B)>i:
            t-=B[i]
        if t>=0:
            C.append(t)
            t=0
        else:
            C.append(t+10)
            t=1
    if pos==0:
        C.append('-')
    while len(C)>0 and C[-1]==0:
        C.pop(-1)
    return C

def mul(A,b):
    t=0
    C=[]
    i=0
    while i<len(A) or t>0:
        if i<len(A) :
            t+=A[i]*b
        C.append(t%10) #当前位
        t=t//10         #进位
        i+=1
    return C


def div(A,b):
    t = 0
    C = []
    for i in range(len(A)-1,-1,-1): #从最高位开始算
        t = t*10+A[i]
        C.append(t//b)
        t = t%b
    C.reverse()#和加减乘除同样
    while len(C)>0 and C[-1]==0:
        C.pop(-1)
    return C,t







if __name__=='__main__':
    A=[7,6]  #A 代表 6,7
    B=[1,6]       #B 代表 6,1
    for x in reversed(add(A,B)):
        print(x,end=' ')
    print()
    for x in reversed(minus(A,B)):
        print(x,end=' ')
    print()
    for x in reversed(mul(A,10)):
        print(x,end=' ')
    print()
    C = div(A,11)
    for x in reversed(C[0]):
        print(x,end=' ')
    print()
    print(C[1])