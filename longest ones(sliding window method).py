def longestones(nums,k):
    n=len(nums)
    maxlen=0
    left=0
    right=0
    count_zeros=0
    while(right < n):
        if(nums[right]==0):
            count_zeros+=1
        if(count_zeros > k):
            while(count_zeros>k):
                if(nums[left]==0):
                    count_zeros-=1
                left+=1
        maxlen=max(maxlen,right-left+1)
        right+=1
    return maxlen
nums=list(map(int,input().split()))#1 1 1 0 0 0 1 1 1 1 0
k=int(input())#2
print(longestones(nums,k))