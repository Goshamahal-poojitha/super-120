from math import *
def KokoEat(arr,k):
    for no_of_banana in range(1,max(arr)+1):
        time=0
        for num in arr:
            time+= ceil(num/no_of_banana)
        if(time<=k):
            return no_of_banana
arr=list(map(int,input().split()))# 3 6 7 11
k=int(input()) #8
print(KokoEat(arr,k))