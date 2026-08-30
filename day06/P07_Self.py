"""
    该案例演示了Self
"""
class Student:
    # 类属性
    school = "atguigu"

    def __init__(self, name, age):
        # 定义实例属性
        self.name = name
        self.age = age

    def study(self):
        # Student.eat(self)
        self.eat()
        print(f"{self.name}吃饱了，开始study....")

    def eat(self):
        print("eating...")

zs = Student("zs",20)
ls = Student("ls",30)

zs.study()
print("~~~~~")
ls.study()
# zs.study()
print(Student.study)
Student.study(zs)