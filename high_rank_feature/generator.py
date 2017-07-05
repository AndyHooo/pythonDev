# coding:utf-8
#生成器generator
#1.将list生成式中的[]直接换成()就可以生成generator
g = (x * x for x in range(10))
print int(g.next())

for n in g:
    print n
