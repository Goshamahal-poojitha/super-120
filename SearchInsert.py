def SearchInsert(arr,target):

    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input().split())) #1 3 5 6
target=int(input()) #2
print(SearchInsert(arr,target)) # 1 [ index place]
