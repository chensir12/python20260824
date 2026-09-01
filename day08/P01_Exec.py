# 编写一个函数，接受一个整数作为参数，返回该整数的反转形式。例如，输入 123，返回 321；输入 -456，返回 -654。
from xml.sax.handler import property_interning_dict


def reverse_int(prama):
    s = str(abs(prama))
    s_ = int(s[::-1]) if prama >= 0 else - int(s[::-1])
    return s_
print(reverse_int(-123))


# 有一个嵌套字典，存储了学生的课程成绩信息。
# 编写一个函数，计算每个学生的平均成绩，并返回一个新的字典，键为学生名字，值为平均成绩。
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}

def get_avg_per_stu(dic2):
    dic = {}
    for key, value in dic2.items():
        print(type(value.values()))
        dic[key] = "{:.2f}".format(sum(value.values())/len(value))
    return dic
print(get_avg_per_stu(students))

# 题目 1：动态添加属性
# 定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。
class Person:
    pass

p1 = Person()
p1.hobby = "readding"
print(p1.hobby)

# 题目 2：动态添加方法
# 定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：S = π r^2），
# 然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用types.MethodType）
class Circle:
    def __init__(self, radius):
        self.radius = radius
import math
def calculate_area(self):
    area = math.pi * self.radius ** 2
    return area
c1 = Circle(2)
import types
c1.calculate_area = types.MethodType(calculate_area, c1)
print(c1.calculate_area())


# 题目 3：封装特性
# 定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），提供一个 deposit 方法用于存钱，
# 一个 withdraw 方法用于取钱，取钱时如果余额不足则打印提示信息。

class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"余额为{self.__balance},不足取{amount}")
        else:
            self.__balance -= amount
            print(f"余额为{self.__balance},取了{amount}")
b = BankAccount(100)
b.withdraw(200)

# 题目 4：多态特性
# 定义一个 Shape 类，有一个抽象方法 area（方法体为空）。再定义 Rectangle 类和 Circle 类继承自 Shape 类，
# 分别实现 area 方法计算矩形面积（长 × 宽）和圆的面积（\(\pi r^2\)）。创建 Rectangle 和 Circle 类的对象，
# 将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
r = Rectangle(100, 200)
c = Circle(100)

list1 = [r,c]
for item in list1:
    print(item.area())


