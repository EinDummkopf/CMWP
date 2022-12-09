from ram import *

num = ''.join('{:0>8}'.format(format(54, 'b')))

s2, s1, s0 = map(int, '000')

_8x8_RAM =[RAM() for i in range(8)]

for i, j in zip(_8x8_RAM, num):
    i(s2, s1, s0, D=int(j), W=1)

for i in _8x8_RAM:
    print(i(s2, s1, s0, D=0, W=0), end='')
print()