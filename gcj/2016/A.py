import sys

T = input()

for i in range(T):
    p = input()
    c = 1
    col = [0 for j in range(10)]

    if p == 0:
        print 'Case #'+str(i+1)+': '+'INSOMNIA'
        continue

    while 1:
        line = str(p*c)
        for j in line:
            if col[int(j)] == 0:
                col[int(j)] = 1
        #print col
        if sum(col) == 10:
            print 'Case #'+str(i+1)+': '+str(p*c)
            break
        if c > 1000:
            print 'Limit broken'
            break
        c += 1
