def getfloor(a,n,x):
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]<=x):
            ans=a[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
def getceil(a,n,x):
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]>=x):
            ans=a[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
a=list(map(int,input().split())) #12 18 20 22 36 48 53 58
n=len(a)
x=int(input())#45
print(getfloor(a,n,x))
print(getceil(a,n,x))

