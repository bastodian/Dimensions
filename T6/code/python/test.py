#!/usr/bin/env python


b = 'ooshdsdhABCDEFGH'
print b

for i in range(len(b)):
    if b[i] == 'E':
        print i
        Count = 1
        for j in b[(i-6):i]:
            print j
            Count += 1
            print 'count = ', Count
            if j == 'B':
                break
print Count

### Returns 3 prime
print b[(i-Count-1):]
### Returns 5 prime
print b[:(i-Count)]
