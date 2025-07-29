a=8
count=0
temp=a
while a:
    a=a>>1
    count+=1
while temp&1==0:
    temp=temp >> 1
    count-=1
print(count)
