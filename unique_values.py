def unique_values(s):
    n=[]
    for i in s:
        if s.count(i)==1:
            n.append(i)
        return i
s=[1,1,2,3,3]
print(unique_values(s))