# coding:utf-8
#高阶函数
#函数名是指向该函数的一个变量，所以函数可以作为参数传入另一个函数
#编写高阶函数，就是让函数的参数能够接收别的函数
def add(x,y,f):
    return f(x) + f(y)

print add(-2, 3, abs)

#1.map(fun,list),map函数需要传入一个函数和一个序列,函数会作用于序列中的每一个元素并产生一个新的序列
def f(x):
    return x * x

l = map(f,[1,2,3,43])
for i in l:
    print i
    
def factorial(x,y):
    return x * y

#2.reduce(fun,list),reduce函数需要传入一个带有两个参数的函数和一个序列,reduce把结果继续和序列的下一个元素做累积计算
print reduce(factorial,range(1,11))

#3.filter(fun,list),filter()会传入一个筛选函数和一个序列,满足条件的序列元素留下来重新组合成一个序列返回
def even(x):
    if x % 2 ==0:
        return True
    else:
        return False
    
f = filter(even,[1,2,3,4,5,6,7,8,9,10])
for i in f:
    print i
    
#4.sorted(list,cmp_fun),sorted排序函数,前面一个是需要排序的序列，后面是排序函数，排序函数可以不传入，默认使用ascii码进行排序

#5.返回函数
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

#6.匿名函数：lambda x: x * x,以lambda开头,冒号前面是参数,匿名函数只能有一个表达式,该表达式的值就是返回值,不用return

#7.偏函数：
import functools
int2 = functools.partial(int, base=2)

