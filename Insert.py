#coding:utf8
#依次把未排序的序列里的元素插入到已排序的序列中
def insert(elist):
    n=len(elist)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if elist[j+1]<elist[j]:
                elist[j+1],elist[j]=elist[j],elist[j+1]

if __name__ == "__main__":
    a=[2,5,1,7,9,4,3,0,13,-4,-8,-1]
    insert(a)
    print(a)