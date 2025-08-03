def fruits_in_basket(fruits):
    n=len(fruits)
    maxlen=0
    for i in range(0,n):  #T.C = O(N**2)
        s=set()
        for j in range(i,n):
            s.add(fruits[j])
            if(len(s)>2):
                break
            maxlen=max(maxlen,j-i+1)
    return maxlen
fruits=list(map(int,input().split())) #3 3 3 1 2 1 1 2 3 3 4
print(fruits_in_basket(fruits))