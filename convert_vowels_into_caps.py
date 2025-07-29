s=input()
result=""
for i in s:
    if i in "aeiou":
        result+=chr(ord(i)-32)
    else:
        result+=i