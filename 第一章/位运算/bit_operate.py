#1、get x的k-th位的数  [0-n-1]
#bit=x>>k&1
def get_(x,k):
    return x>>k&1

#2、low_bits 返回n的最后一位1: bits = x&-x
def low_bit(x):
    return x&-x


a=100
print(low_bit(a))