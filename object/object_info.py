#coding:utf-8
import types
#判断基本数据类型可以使用type()方法
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type({}) == types.DictType
print type(int) == types.TypeType
print type(float) == types.TypeType

#对于类类型的需要使用isinstance(ref,type),能用type()判断的也能使用isinstance()来判断
#ref:需要判断的变量的名称,Type:目标类型,判断变量ref是不是type类型
print isinstance([], types.ListType)

#使用dir(object)方法获取一个对象的所有的属性和方法
for n in dir('andy'):
    print n.upper()
    
#getattr(obj,attr) or getattr(obj, attr, defaultVal)、setattr(obj,attr,value)以及hasattr(obj,attr)，我们可以直接操作一个对象的状态
