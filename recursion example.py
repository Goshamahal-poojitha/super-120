def fun(n):#  double recursion example
    if n<=1: 
        return 1
    fun(n-1)
    fun(n-2)
    print(n)
print(fun(5))