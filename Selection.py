#coding:utf8
#在未排序的数组中每次选取最小最大的数依次放到已经排序序列的末尾

def selection(elist):
    n = len(elist)
    for i in range(n):
        for j in range(i+1,n):
            if elist[j]<elist[i]:
                elist[j],elist[i]=elist[i],elist[j]

if __name__ == "__main__":
    a=[2,5,1,7,9,4,3,0,13,-4,-8,-1]
    selection(a)
    print(a)