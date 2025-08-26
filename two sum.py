def twoSum(nums,target):
    n=len(nums) #t.c = O(n)
    low=0
    high=n-1
    while(low<high):
        sum=nums[low]+nums[high]
        if(sum==target):
            return "yes"
        elif(sum>target):
            high-=1
        elif(sum<target):
            low+=1
    return "no"
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))