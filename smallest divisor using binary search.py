from math import *
def smallestdiv(arr,k):
    low=1
    high=max(arr)
    while(low<high):
        div=(low+high)//2
        sum=0
        for num in arr:
            sum+= ceil(num/div)
        if(sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int,input().split())) # 1 2 5 9
k=int(input()) # 6
print(smallestdiv(arr,k))