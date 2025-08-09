def longest_substring(arr,k):
    n=len(arr)
    d={}
    sum=0
    maxlen=0
    for i in range(0,n):
        sum=arr[i]
        if(sum==k):
            maxlen=i+1
        rem=sum-k
        if(rem in d):
            maxlen=max(maxlen,i-d[rem])
        if(sum not in d):
            d[sum]=i
    return maxlen
arr=list(map(int,input().split()))
k=int(input())
print(longest_substring(arr,k))