# coding:utf-8
#列表生成器
sum = 0
for i in range(1,10):
    sum += i
print sum

#生成复杂list
[x * x for x in range(1, 11)]
#>>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 11) if x % 2 == 0]
#>>> [4, 16, 36, 64, 100]

[m + n for m in 'ABC' for n in 'XYZ']
#>>> ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.iteritems()]
#>>> ['y=B', 'x=A', 'z=C']

#大小写转换
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
#>>> ['hello', 'world', 'ibm', 'apple']