from ram import *

M = RAM()

num = list(reversed("{:0>8}".format(format(54, 'b'))))

for i in range(8):
   addr = "{:0>3}".format(format(i, 'b'))
   M(int(addr[2]), int(addr[1]), int(addr[0]), int(num[i]), 1)

stored_num = ''.join(list(reversed(M.stored())))
print(stored_num)
print(int(stored_num, 2))