def search(arr,key):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        if(arr[low]<=arr[mid]):
            if(arr[low]<=key<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=list(map(int,input().split())) #7 8 9 1 2 3 
key=int(input())#4 searching 4 in the arr
print(search(arr,key)) #4 is in 6th index

