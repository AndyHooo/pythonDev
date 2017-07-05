#coding: utf-8
import os
import re
#文件的读写操作
# try:
#     f = open('C:\\Users\\Andy\\Desktop\\test.txt','r')
#     content = f.read()
#     print content
# except IOError,e:
#     print '文件找不到!'
# finally:
#     f.close()
#     
# with open('C:\\Users\\Andy\\Desktop\\test.txt','r') as f:
#     print f.read()
    
# f = open('c:\\Users\\Andy\\Desktop\\test.txt','r')
# for line in f.readlines():
#     print line.strip() #.strip()可以去掉每一行结尾处的\n
    
#读取非ascii码的文件,需要使用rb模式
# img = open('c:\\Users\\Andy\\Desktop\\IMG_0608.JPG','rb')
# print img.read()

#文件的写操作
# with open('C:\\Users\\Andy\\Desktop\\test.txt','w+') as f:
#     f.write('sb')
    
print os.getcwd() #得到当前工作目录，即当前Python脚本工作的目录路径
for fileName in os.listdir('C:\\Users\\Andy\\Desktop'): #返回指定目录下的所有文件和目录名
    print fileName
# os.remove('c:\\Users\\Andy\\Desktop\\IMG_0608.JPG') #删除指定文件
# os.removedirs(r"c：\python") #删除多个目录
if os.path.isfile('C:\\Users\\Andy\\Desktop\\test.txt'): #检验一个路径是否是文件
    print '是文件'

os.path.isabs('C:\\Users\\Andy\\Desktop\\test.txt') #判断一个路径是否为绝对路径

os.path.exists('C:\\Users\\Andy\\Desktop\\test.txt') #判断一个路径是否存在

os.path.split('C:\\Users\\Andy\\Desktop\\test.txt') #返回一个路径的目录名和文件名:('C:\Users\Andy\Desktop', 'test.txt')
#http://www.jb51.net/article/47999.htm
print os.name


