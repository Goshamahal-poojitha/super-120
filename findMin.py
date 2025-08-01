def findMin(arr):
    low=0
    high=len(arr)-1
    min=float("inf")
    while(low<=high):
        mid=low+high //2
        if arr[low]<=arr[mid]:
            if(arr[low]<=min):
                min=arr[low]
            low=mid+1
        elif(arr[low]<=arr[high]):
            if(arr[mid]<=min):
                min=arr[mid]
            high=mid-1
    return min
arr=list(map(int,input().split())) # 7 8 9 2 3 4
print(findMin(arr))