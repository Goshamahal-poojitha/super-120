def generate(ind,curr_str,o,c,ans,n):
    if(o>n):
        return
    if(ind==2*n and o==c):
        ans.append(curr_str)
        return
    generate(ind+1,curr_str+"(",o+1,c,ans,n)
    if(o>c):
        generate(ind+1,curr_str+")",o,c+1,ans,n)
def generateparenthesis(n):
    ind=0
    o=0
    c=0
    curr_str=""
    ans=[]
    generate(ind,curr_str,o,c,ans,n)
    return ans
n=int(input())
print(generateparenthesis(n))
 