def l_m_s(s):
    return min(s[i] + s[:i] + s[i+1:] for i in range(len(s)))
         #i=2    #s[2]+s[:2]+s[3:1] 
                 #n+ba+ana
s = input()#banana
print(l_m_s(s))
