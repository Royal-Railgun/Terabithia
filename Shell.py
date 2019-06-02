#coding:utf8
def shell(elist):
    gap = len(elist)//2
    while gap>0:
       for i in range(gap,len(elist)):
           j=i
           while j>=gap:
               if elist[j]<elist[j-gap]:
                   elist[j],elist[j-gap]=elist[j-gap],elist[j]
               j-=gap
       gap = gap//2

if __name__ == "__main__":
    a=[2,5,1,7,9,4,3,0,13,-4,-8,-1]
    shell(a)
    print(a)