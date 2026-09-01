"""
    该案例演示了在子类中复用父类成员
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
        print("先吃点东西")
        # 通过super()方式访问父类成员
        super().eat()
        # 通过父类名.成员名
        Person.eat(self)
        print("studying...",Person.home)

class ChineseStudent(Student, YellowRace):  # 继承了Student和YellowRace
    """中国学生"""
    country = "中国"

zs = ChineseStudent("zs","1年级")
zs.eat()
zs.study()