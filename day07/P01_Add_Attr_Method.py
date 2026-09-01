"""
    该案例演示了动态的添加属性以及方法
"""
import types


class Person:
    def __init__(self,name):
        self.name = name
"""
# 动态给对象添加属性
p1 = Person("chj")
print(p1.name)
p1.age = 20
print(p1.age)

p2 = Person("xyz")
# print(p2.age)
"""
"""
# 动态给类添加属性
p1 = Person("ls")
Person.school = "sgg"
print(p1.school)
p2 = Person("zs")
print(p2.school)
"""
"""
# 在类外定义的函数
def f1(self, x, y):
    return x & y
class C:
    f = f1
print(C().f(6,13))
"""
"""
# 动态给实例添加方法
# 1)添加普通方法
class Person:
    def __init__(self,name = None):
        self.name = name

def eat():
    print("吃饭")

p1 = Person()
p1.ff = eat
p1.ff()
# 2)添加实例方法
def laugh(self):
    print(f"{self.name}在笑")
p2 = Person("ls")
# 给对象添加的实例方法只绑定在当前对象上，不对其他对象生效，而且需要传入 self 参数。需要使用 types.MethodType(方法名，实例对象) 来添加实例方法
p2.laugh = types.MethodType(laugh,p2)
p2.laugh()
"""
"""
# 动态给类添加方法
class Person:
    home = "earth"
    def __init__(self,name=None):
        self.name = name
# 定义类方法
@ classmethod
def come_from(cls):
    print(f"来自{cls.home}")
# 定义静态方法
@staticmethod
def static_function():
    print("static_function")
Person.come_from = come_from
Person.come_from()
Person.static_function = static_function
Person.static_function()
"""
"""
# 动态删除属性与方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
zs = Student("zs",20)
print(zs.name)
print(zs.age)
# del 对象.属性名
del zs.age
# delattr(对象，属性名)
# delattr(zs,"age")
print(zs.name,zs.age)
"""
"""
# __slots__限制实例属性与实例方法
class Person:
    __slots__ = ("name","age","eat")

    def __init__(self,name = None):
        self.name = name
def eat(self):
    print(f"{self.name}在吃饭")
def drink(self):
    print(f"{self.name}在喝水")
p = Person("张三")

# 添加实例属性
p.age = 20
print(p.age)

# 添加实例方法
p.eat = types.MethodType(eat,p)
p.eat()

# 添加slots里面没有的实例属性
# p.weight = 100

# 添加slots里面没有的实例方法
# p.drink = types.MethodType(drink,p)
"""

# 不建议类属性和实例属性同名，实例属性和方法同名 即使同名以后应该有一个访问的顺序
class Person:
    aa = "类属性"
    def __init__(self):
        self.aa = "实例属性"
        pass

    def aa(self):
        print("实例方法")

p = Person()
print(p.aa)
print(Person.aa)
# p.aa() # 报错
Person.aa(p)

"""
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __init__(self):
        print("1234")
# p = Person("Zs",20)
p = Person()
"""
