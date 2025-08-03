def floorsqrt(n):
    ans=0
    low=1
    high=n
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid <=n):
            ans=mid
            low=mid+1
        elif(mid*mid > n):
            high=mid-1
    return ans
n=int(input()) #25 or 28
print(floorsqrt(n))
