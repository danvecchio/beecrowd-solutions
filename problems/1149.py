# -*- coding: utf-8 -*-
entrada = input()
li = list(entrada.split(" "))
result = 0
for i in range(0,int(li[-1])):
  result = result + int(li[0]) + i
print (result)