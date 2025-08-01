#5 7 7 8 8 10
#target=6
def getlowerBound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def getUpperbound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]<target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=list(map(int,input().split()))
target=int(input())
lb=getlowerBound(nums,target)
ub=getUpperbound(nums,target)

print(lb,ub)



