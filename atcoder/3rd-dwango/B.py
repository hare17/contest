# -*- coding:utf-8 -*-

# ニコニコレベル

T = raw_input().strip()
ans = 0


for i in range(2):
    t = 0
    for j in range(len(T)):
        c = "25"[(i+j)&1]
        if (T[j] == c or T[j] == "?") and (c=="2" or t > 0):
            t += 1
            ans = max(ans. t/2*2)
        else:
            t = 0
print ans

 
