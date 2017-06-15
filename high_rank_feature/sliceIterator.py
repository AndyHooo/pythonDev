#coding:utf-8
#1.切片:取一个list或tuple的部分元素L[x:y],对list取下标x到下标y(不包括),不写的话默认为0
from collections import Iterable
nums = [1,2,3,4,54,6,6,4,5675,454]
nums[0:2]
nums[:2] #等价于nums[0:2]

nums[-2:] #可以倒序切片

nums[:10:2] #前10个数，每两个取一个

nums[::2] #所有的数每两个取一个

nums[:] #复制一个list

#2.迭代：
#dict迭代
#(1).只迭代key
names = {'andy':'1','omni':'0'}
for key in names:
    print key
    
#(2).只迭代value
for value in names.itervalues():
    print value
    
#(3).同时迭代key和value
for k,v in names.iteritems():
    print k +","+v
    
#3.判断一个对象是否可以迭代:通过collections模块的Iterable类型判断
if isinstance(names,Iterable):
    print '可以迭代'
else:
    print '不能迭代'
    
##Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(names):
    print 'names[' + str(i) + "]:" + value
    
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y


