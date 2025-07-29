def fun(n):# recursion example
    if n==1:
        fun(n-1)
    return n
print(fun(5)) 