# coding:utf-8
# 函数的参数
#1.默认参数：
def my_pow(x,n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

result = my_pow(2)
print result

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city
    
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

##Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

#2.可变参数:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做,推荐使用第二种方法
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
calc(*nums)

#3.关键字参数：而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
    for x in kw:
        print kw[x]
    
person('andy',20,job='java',email='396877565@qq.com')
kwDict = {'job':'java','email':'396877565@qq.com'}
person('andy', 20,**kwDict)
