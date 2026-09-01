"""
    该案例演示了方法的解析顺序  MRO
"""
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
        print("先吃再学")
        Person.eat(self)
        print("studying...")

class ChineseStudent(YellowRace,Student):

    country = "中国"

y1 = ChineseStudent("张三", "三年级")

print(ChineseStudent.__mro__)