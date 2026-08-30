"""
    该案例演示了属性
"""
"""
# 类属性
class Person:
    # 定义在类中，方法外
    home = "earth"

# 1）通过 类名.属性名 或 实例名.属性名 访问
print(Person.home)
print(Person().home)

# 2）通过 类名.属性名 添加与修改类属性
print(Person.home)
Person.home123 = "地球"
print(Person.home,Person.home123)

# 注意： 若使用 实例名.属性名 则会创建或修改实例属性  所以：类属性和实例属性不要同名
p1 = Person()
p2 = Person()
print(p1.home)
print(p2.home)
p1.home = "地球"
print("~~~~")
print(p1.home)
print(p2.home)
print(Person.home)
"""

"""
# 实例属性
class Person:
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
    pass

# 1）通过 实例名.属性名 访问
# p1 = Person("zs",20)
# print(p1.name)
# print(p1.age)

# 2）通过 实例名.属性名 添加与修改实例属性
p1 = Person()
p1.name = "zs"
p1.age = 18
p1.age = 20
print(p1.name)
print(p1.age)
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("zs",20)
p2 = Person("ls",30)
print(p1.name,p1.age)
print(p2.name,p2.age)
p1.gender = "male"
print(p1.name,p1.age,p1.gender)
# print(p2.gender)
print(dir(Person))
