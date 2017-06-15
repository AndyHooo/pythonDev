#coding: utf-8
'''
创建Person类:person类的所有的属性都是共有的,外部可以随意修改
'''
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_stage(self):
        age = self.age
        if age <= 6:
            return 'child'
        elif age <= 18:
            return 'teenager'
        else:
            return 'adult'
p = Person('andy',26)
stage = p.get_stage()
print stage

class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self,name):
        self._name = name
        
    def set_age(self,age):
        self._age = age
        