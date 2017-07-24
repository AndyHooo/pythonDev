#coding: utf-8
#hashlib提供常见的摘要算法,如:MD5,SHA1
import hashlib
md5 = hashlib.md5()
s = 'how to use md5 in python hashlib?'
md5.update(s)
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update(s)
print sha1.hexdigest()