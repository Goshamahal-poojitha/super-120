def longest_substring(s,k):
    n=len(s)
    maxlen=0
    left=0
    right=0
    d={}
    while(right<n):
        if(s[right] in d):
            d[s[right]]+=1
        else:
            d[s[right]]=1
        if(len(d)>k):
            while(len(d)>k):
                d[s[left]]-=1
                if(d[s[left]]==0):
                    del d[s[left]]
                left+=1
        maxlen=max(maxlen,right-left+1)
        right+=1
    return maxlen
s=input()#aaabbccd    
k=int(input())#2
print(longest_substring(s,k))