#count digits in int
def fun(n):
    if n==0: 
        return 
    print(n,end=" ")
    fun(n-1)
    print(n,end=" ")
print(fun(5))