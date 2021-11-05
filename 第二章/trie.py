#trie 高效的字符串存储 和查询方法
#ord() 转圜为 ascii码数字
#ascii转化为字符串

N = int(10e6+10)
son =[ [0]*26 for i in range(N)] #son[][]存储树中每个节点的子节点
cnt = [0]*N#记录 结尾节点 标记
idx = 0#保存每次插入字符的下标 0号点既是根节点，又是空节点
'''
def insert(str):
    p=0
    for char in str:
        char=ord(char)-ord('a')
        if son[p][char]==0:
            global idx
            idx+=1
            son[p][char]=idx
        p=son[p][char]
    cnt[p]+=1
def queue(str):
    p=0
    for char in str:
        char = ord(char)-ord('a')
        if son[p][char]==0:
            return 0
        p=son[p][char]
    
    return cnt[p]
    
'''

def insert(str):
    p=0#每次从根节点插入
    for char in str:
        char=ord(char)-ord('a') #转化为0-25

        if(son[p][char]==0):#节点不存在
            global idx
            idx=idx+1
            son[p][char]=idx#插入新节点

        p=son[p][char]#继续寻找
    cnt[p]+=1#添加一个单词结尾标记

def queue(str):#查询
    p=0
    for char in str:
        char=ord(char)-ord('a')
        if(son[p][char]==0):#没有该路径
            return 0
        p=son[p][char]

    return cnt[p]#查看该单词的数量 》=0





#最大异或对：在给定的 N 个整数 A1，A2……AN 中选出两个进行 xor（异或）运算，得到的结果最大是多少？
intson=[[0]*2 for i in range(N)]
intcnt=[0]*N
intidx=0

def insert_A(A):
    p=0
    for i in range(32):
        bit=(A>>i)&1
        if intson[p][bit]==0:#没有该节点
            global intidx
            intidx+=1
            intson[p][bit]=intidx#插入节点
        p=intson[p][bit]
    intcnt[p]+=1
'''
用Trie（字典树），建树时，根据每个数字的对应的二进制串构造一个二叉树，每个结点两个分支，
分支指向的两个son结点分别表示当前位的数值为0或1，记录每次输入的数字转化成的二进制串，当前位为1，就走到数值为1的结点，否则走到0结点，这样每个数字对应的Trie中的路径就是唯一的。
因为要求异或值最大，所以用贪心的思想，在第一个数字固定的情况下，尽可能地让第二个数的每一位都与第一个数的对应位相反，
这样最终确定的第二个数与第一个数的异或值就最大，所以在查询时，遍历第一个串o（n），根据固定的第一个二进制串，每次尽可能走到与当前位的值相反的结点，
这样的路径对应的就是与第一个二进制串异或值最大的二进制串，便利了这个数的位数次o（logn），所以总的时间复杂度o（n*logn）；


'''
def findmax(list_A):
    for A in list_A:
        insert_A(A)
    res=0
    for A in list_A:
        p=0
        tmp=0
        for i in range(31):
            bit=(A>>i)&1
            op_bit=0 if bit==1 else 1

            if intson[p][op_bit]!=0:
                p=intson[p][op_bit]
                tmp|=(1<<i)#该位抑或结果为1
            else:
                p=intson[p][bit]
                #抑或结果为0
        res=max(res,tmp)
    return res


if __name__=='__main__':
    #insert('adada')
    #insert('dsada')
    #insert('adada')
    #print(queue('adada'))
    list_A=[1,2]
    print(findmax(list_A))