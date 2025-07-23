def aggressive_cows(minDist,stalls,k):
    cow=stalls[0]
    placedCows=1
    for stall in range(1,len(stalls)):
        if(stalls[stall]-cow>=minDist):
            cow=stalls[stall]
            placedCows+=1
        if(placedCows>=k):
            return True
    if(placedCows<k):
        return False
stalls.sort()
stalls=list(map(int,input().split()))
k=int(input())   
Min=min(stalls)
Max=max(stall)
if(k==2):
    return max-Min
for minDist in range(1,max-Min+1):
    if(aggressive_cows(minDist,stalls,k)):
        continue
    else:
        return minDist-1



            