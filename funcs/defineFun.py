#coding:utf-8
#1.函数定义:
#在Python中，定义一个函数要使用def语句，
#依次写出函数名、括号、括号中的参数和冒号:，
#然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#我们以自定义一个求绝对值的my_abs函数为例：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
#因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
#return None可以简写为return。

#2.空函数
def nop():
    pass

#3.参数检查
#(1).调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
#(2).调用函数时，参数类型不对，python编译器不会自动检查出来,可以在调用前对参数进行校验
#比如:对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现：
def my_abss(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#4.函数返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

##注意：原来返回值是一个tuple！
#但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便