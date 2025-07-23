n=input() #n=153 or n=343
power=len(n)
arm=0
for i in n:
    arm+=int(i)**power
if arm==int(n):
    print("armstrong")
else:
    print("not an armstrong")