#coding:utf8
#对比相邻的两个元素，大的往后移
def Bubble(elist):
    n=len(elist)
    found = True
    for i in range(n):
        for j in range(n-i-1):
            if elist[j] > elist[j+1]:
                elist[j],elist[j+1] = elist[j+1],elist[j]
                found = False
        if found:
            return
def hello():
    pass
if __name__ == "__main__":
    a=[2,5,1,7,9,4,3,0,13,-4,-8,-1]
    # a=[1,2,4,5,7,8,9]
    Bubble(a)
    print(a)
    


