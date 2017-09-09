# -*- coding: utf-8 -*-

import sys

t = input()

for i in xrange(t):
    s, k = sys.stdin.readline().rstrip().split();
    stat = '+'
    cnt = 0
    for j in xrange(len(s)):
        #print '試行: ', cnt, s[j], stat
        if s[j] != stat:
            cnt += 1
            stat = s[j]
    
    print 'Case #' + str(i+1) + ':',
    if cnt == 0:
        print 0
    else:
        if k > cnt / 2 + 1:
            print cnt / 2 + 1
        else:
            print 'IMPOSSIBLE'




