# -*- coding: utf-8 -*-
num = int(input())
print('N[0] =', num)
for i in range(1,10):
    num*=2
    print(f'N[{i}] = {num}')