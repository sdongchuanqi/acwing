# s[]是长文本，p[]是模式串，n是s的长度，m是p的长度
# 求模式串的Next数组：
#str= ' str' 下标为1开始
#pat=' pat'  下标为1开始
#思想 每次不回退下标str的遍历下标i，而是改变j的位置到最大前缀
#

def next(pat):

    i,j=2,0
    m=len(pat)
    ne=[0]*m

    while i<m:
        while j>0 and pat[i]!=pat[j+1]:
            j=ne[j]
        if pat[i]==pat[j+1]:#找到 满足pat[i]=pat[j+1]的 j
            j+=1  #把pat[i]考虑在内

        ne[i]=j# j=0表示没有找到满足 pat[i]=pat[j+1]位置

        i+=1
    return ne

def KMP(pat,str):
    # 匹配过程
    ne = next(pat)
    i, j, n, m = 1, 0, len(str) - 1, len(pat) - 1
    while i <= n:
        while j > 0 and str[i] != pat[j + 1]:#寻找最大前缀后缀
            j = ne[j]
        if str[i] == pat[j + 1]:
            j += 1

        if j == m:
            j = ne[j]  # 匹配成功后：使得j成为ne[j]为继续进行下一次匹配i位置做准备
            print('匹配成功%d' % (i - (m - 1) + 1))
        i += 1


def KMP(pat,str):

    def next(pat):
        m=len(pat)
        ne=[0]*m
        i,j=2,0#next[1]=0 前缀 后缀定义  所以i从2开始
               #next[j]表示 pat[1:j+1]的最大相等前缀后缀
               #pat=' ABABCABBA'
        while i<m:
            while j>0 and pat[i]!=pat[j+1]:#对 pat[i] 和 pat[j+1]进行比较
                                           #表示 pat[j]都是已经匹配好了
                                           #即pat[1:j+1]=pat[i-j:i]
                                           #如果当前位置pat[i]不能和pat[j+1]匹配
                                           #那么就找pat[1:j+1]的最大前缀后缀

                                           #由于 pat[1:j+1]本身就是最大前缀后缀 即pat[1:j+1]=pat[i-j:i]
                                           #pat[1:j+1]的最大前缀后缀 pat[1:ne[j]+1]满足 pat[1:ne[j]+1]=pat[j-ne[j]+1:j+1]

                                           #也满足：pat[1:ne[j]+1]=pat[j-ne[j]+1:j+1]=pat[i-ne[j]:i]
                                           #[1..j]sdasdd[i-j..i] = 串test

                                           #ne[j]同时是 [1..j]和[i-j..i]的最大前缀后缀，即是 串test的次最大前缀后缀
                                           #即ne[j]是次最大前缀后缀
                j=ne[j]

            if pat[i]==pat[j+1]:#找到了某个前缀后缀 而且 满足 当前第i个字符等于第j+1个字符
                j+=1            #更新当前i的ne为j+1
            ne[i]=j
            i+=1
        return ne

    #匹配过程
    ne=next(pat)
    i,j,n,m=1,0,len(str)-1,len(pat)-1
    while i<=n:
        while j>0 and str[i]!=pat[j+1]:
            j=ne[j]
        if str[i]==pat[j+1]:
            j+=1

        if j==m:
            j=ne[j]#匹配成功后：使得j成为ne[j]为继续进行下一次匹配i位置做准备
            print('匹配成功%d'%(i-(m-1)+1))
        i+=1
if __name__=='__main__':
    KMP(' koko',' kokokokoplp')
