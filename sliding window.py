arr=list(map(int,input().split()))# 5 10 8
n=len(arr)
for i in range(0,n):
    for j in range(i,n):
        print(arr[i:j+1])
        