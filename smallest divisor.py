from math import *
def smallestDivisor(arr,k):
    for div in range(1,max(arr)+1):
        sum=0
        for num in arr:
            sum += ceil(num/div)
        if(sum<=k):
            return div
arr=list(map(int,input().split())) # 1 2 5 9
k=int(input()) #6
print(smallestDivisor(arr,k))