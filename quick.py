#coding:utf8
#选择一个基准值，然后小的放一边，大的放一边
#再递归
#!!!!!!!!!!返回的是一个新列表，而不是在原来列表上改动的
def quick(elist):
    if elist == []:
        return []
    pivot = elist[0]
    less = quick([x for x in elist[1:] if x < pivot])
    more = quick([y for y in elist[1:] if y >= pivot])
    return less + [pivot] + more

if __name__ == "__main__":
    a=[2,5,1,7,9,4,3,0,13,-4,-8,-1]
    print(quick(a))
