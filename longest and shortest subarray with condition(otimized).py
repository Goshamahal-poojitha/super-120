arr=list(map(int,input().split()))#1 3 2 1 2 11 14 3
k=int(input())#10
n=len(arr)
maxlen=0
left=0
right=0
sum=0
while(right<n):
    sum+=arr[right]
    while(sum>k):
        sum-=arr[left]
        left+=1
    maxlen=max(maxlen,right-left+1)
    right+=1
print(maxlen) #5
        