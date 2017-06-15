# coding:UTF-8
#dict:python中的键值对存值{}
scoreDict = {'andy':100,'xiaoming':60}

#取值
andyScore = scoreDict['andy']
print andyScore

#如果遇到不存在的键时会报错,为了避免键不存在报错：
#1.使用 'andy' in scoreDict 判断dict中是否存在相应键
key = 'andy'
if key in scoreDict:
    andyScore = scoreDict[key]
    
#2.通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
andyScore = scoreDict.get(key)

#删除一个key,使用pop()方法
scoreDict.pop(key)

##set:
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合,重复元素在set中自动被过滤
s = set([1, 2, 3])

#通过add(key)方法添加元素
s.add(4)

#通过remove(key)删除元素
s.remove(2)

#取并集和交集
s1 = set([1,2,3,4])
s2 = set([2,3,4])

s1 | s2
s1 & s2