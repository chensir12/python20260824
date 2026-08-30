"""
    该案例演示了对象的创建过程
"""
class Student:
    # 类属性
    school = "atguigu"

    def __init__(self, name, age):
        # 定义实例属性
        self.name = name
        self.age = age

    # 定义实例方法
    def study(self):
        print("study....")

wzh = Student("wzh", 20)
print(wzh.school)
print(wzh.name)
print(wzh.age)
# 语法糖
Student.study(wzh)
wzh.study()

