def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return True
        elif(arr[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return False
arr=list(map(int,input().split())) # 1 2 3 4 5 6 7 8 # list must be in sorted order
target=int(input())     # 7
print(binarysearch(arr,target)) # true