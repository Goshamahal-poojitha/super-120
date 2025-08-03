def totalfruits(fruits):
    n = len(fruits)
    left = 0
    right = 0
    maxlen = 0
    d = {}
    while right < n: 
       
        if fruits[right] in d:
            d[fruits[right]] += 1
        else:
            d[fruits[right]] = 1
       
        while len(d) > 2:
            d[fruits[left]] -= 1
            if d[fruits[left]] == 0:
                del d[fruits[left]]
            left += 1
        maxlen = max(maxlen, right - left + 1)
        right += 1
    return maxlen
fruits = list(map(int, input().split()))#3 3 3 1 2 1 1 2 3 3 4
print(totalfruits(fruits))
