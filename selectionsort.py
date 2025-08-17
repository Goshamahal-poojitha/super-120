def selectionSort(arr):
    for i in range(0,len(arr)):
        Min=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[Min]):
                Min=j
        arr[i],arr[Min]=arr[Min],arr[i]
    return arr
arr=list(map(int,input().split()))
print(selectionSort(arr))