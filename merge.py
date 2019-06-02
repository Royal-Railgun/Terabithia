#coding:utf8

def merge1(elist):
    if len(elist)<=1:
        return elist
    mid = len(elist)//2
    left = merge1(elist[:mid])
    right = merge1(elist[mid:])
    return merge2(left,right)

def merge2(left,right):
    l,r=0,0
    result =[]
    while l<len(left) and r < len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result=result+left[l:]
    result=result+right[r:]
    return result

if __name__ == "__main__":
    a=[2,5,1,7,9,4,3,0,13,-4,-8,-1]
    print(merge1(a))




