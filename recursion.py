def fun(n):#  double recursion example
    if n<=1: 
        return 1
    fun(n-1)
    print(n)
    fun(n-3)
   
print(fun(5))