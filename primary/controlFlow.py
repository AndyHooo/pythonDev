# coding: UTF-8
#条件控制
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'child'

#for循环
nums = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for num in nums:
    sum += num
print sum

#计算0-100的和,可以使用range(101)产生一个0-100的list
sum = 0
for n in range(101):
    sum += n
print sum

#while循环(计算0-100的和)
last = 100
sum = 0
while last >= 0:
    sum += last
    last = last - 1
print 'while循环结果:'+str(sum)

#raw_input()方法读取的内容是字符串
age = int(raw_input("请输入年龄:"))
if age >= 2000:
    print '00后'
elif age >= 1980:
    print '90后'
