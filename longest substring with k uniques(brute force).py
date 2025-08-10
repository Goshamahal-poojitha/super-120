def longest_substring(s,k):
    n=len(s)
    maxlen=0
    if(n==1):
        return 
    dup=sorted(s)
    if(dup[0]==dup[n-1]):
        return -1
    if(len(set(dup))<k):
        return -1
    maxlen=0
    for i in range(0,n):
        hash_set=set()
        for j in range(i,n):
            hash_set.add(s[j])
            if(len(hash_set)>k):
                break
            maxlen=max(maxlen,j-i+1)
    return maxlen
s="aaabbccd"
k=int(input())
print(longest_substring(s,k))