from math import *
def KokoEat(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        no_of_bananas=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/no_of_bananas)
        if(time<=k):
            high=no_of_bananas-1
        else:
            low=no_of_bananas+1
    return low
arr=list(map(int,input().split()))# 3 6 7 11
k=int(input()) #8
print(KokoEat(arr,k))