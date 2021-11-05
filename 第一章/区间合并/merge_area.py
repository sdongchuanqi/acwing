#1、按照左边界排序
#2、给定当前区间 [sta_1,end_1]
#   1、如果下一个区间的左边界sta_2>end_1 添加当前区间到答案 并把当前区间更新为下一个区间
#   2、如果下一个区间的左边界sta_2<=end_1
#   2、  1、如果下一个区间end_2>end_1 更新end_1=end_2
#   2、  2、下一个区间end_2<=end_1 不更新end_1

def merge(segs):
    st,ed=-2e9,-2e9
    res=[]

    for seg in segs:
        if ed<seg[0]:
            if st!=-2e9:
                res.append([st,ed])
            st,ed=seg[0],seg[1]
        else:
            if ed<seg[1]:
                ed=seg[1]
    return res