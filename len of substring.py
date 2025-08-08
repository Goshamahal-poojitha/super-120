def lenofsubstring(s):
    n=len(s)
    maxlen=0
    for i in range(0,n):
        checker=[0]*256
        for j in range(i,n):
            if(checker[ord(s[j])]==1):
                break
            checker[ord(s[j])]==1
            maxlen=max(maxlen,j-i+1)
    return maxlen
s="ABCAA"
print(lenofsubstring(s))