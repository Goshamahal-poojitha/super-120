arr=list(map(int,input().split()))# 2 3 5 8 10 12 3 1
k=int(input())#4
n=len(arr)
left=0
right=k-1
sum=sum(arr[left:right+1])
maxsum=sum
while(right< n-1):
    sum-=arr[left]
    left+=1
    right+=1
    sum+=arr[right]
    maxsum=max(maxsum,sum)
print(maxsum) #35
        