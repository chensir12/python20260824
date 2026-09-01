"""
    该案例演示了多继承
"""
"""
# 调用方法时先在子类中查找，若不存在则从左到右依次查找父类中是否包含方法。
class Person:

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")

class YellowRace(Person):

    color = "yellow"

    def run(self):
        print("runing...")

class Student(Person):

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("studying...")

class ChineseStudent(Student,YellowRace):
    country = "China"

zs = ChineseStudent("Zs","一年级")
print(zs.country,zs.name,zs.grade,zs.color,zs.home)
zs.study()
zs.run()
zs.eat()
"""
class Person:

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")

    def m1(self):
        print("Person m1无参")

class YellowRace(Person):

    color = "yellow"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("runing...")

    def m1(self):
        print("YellowRace m1无参")

class Student(Person):

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("studying...")

    def m1(self):
        print("student m1无参")

class ChineseStudent(Student,YellowRace):
    country = "China"
    def __init__(self):
        print("init")

    # def m1(self):
    #     print("m1无参")
    #
    # def m1(self,a):
    #     print("m1带参数")

    def m1(self,*args):
        print("m1无参",args)

zs = ChineseStudent()
zs.m1()
zs.m1(1)
zs.m1(1,"aa")