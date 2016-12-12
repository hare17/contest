import sys

line = sys.stdin.readline().rstrip()

i = len(line)
while i > 0:
    if line[i-5:i] == 'dream':
        i -= 5
    elif line[i-5:i] == 'erase':
        i -= 5
    elif line[i-7:i] == 'dreamer':
        i -= 7
    elif line[i-6:i] == 'eraser':        
        i -= 6
    else:
        print 'NO'
        sys.exit()
print 'YES'        
