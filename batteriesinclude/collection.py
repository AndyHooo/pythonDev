#coding: utf-8
from collections import namedtuple
from _collections import defaultdict
#namedtuple:namedtuple('名称', [属性list]),
#namedtuple是一个函数，它用来创建一个自定义的tuple对象,
#并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素.
#这样一来，我们用namedtuple可以很方便地定义一种数据类型,
#它具备tuple的不变性，又可以根据属性来引用，使用十分方便
Circle = namedtuple('circle',['x','y','r'])
c = Circle(1,2,3)
print isinstance(c, Circle)


#deque,deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈.
from collections import deque
d = deque(['a','b','c'])
d.append('d')
d.appendleft('e')
d.pop()
d.popleft()
for i in d:
    print i
    
#defaultdict:使用dict时,如果引用的Key不存在,就会抛出KeyError.
#如果希望key不存在时,返回一个默认值，就可以用defaultdict:
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'nihao'
print dd['key1']
print dd['key2']


#OrderedDict:在使用dict的时候,key是无序的,如果希望key是有序的,
#可以使用OrderedDict
from collections import OrderedDict
d = dict([('1','a'),('2','b'),('3','c')])
for i in d.values():
    print i
od = OrderedDict([('1','a'),('2','b'),('3','c')])
for i in od.values():
    print i
for k in od.keys():
    print k
    

#Counter:Counter是一个简单的计数器.
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
for k,v in c.iteritems():
    print k + ":" + str(v)
