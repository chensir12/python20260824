"""
    该案例演示了方法
"""
"""
# 实例方法
# 	实例方法在类中定义，第一个参数为self，代表实例本身。
# 	实例方法只能被实例对象调用。
# 	可以访问实例属性、实例方法、类属性、类方法。
class Student:
    school = "atguigu"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play_game(self):
        self.eat()
        print(f"{self.age}岁的{self.name}正在{self.school}聚精会神的玩着游戏")

    def eat(self):
        print("先吃点东西")


wzh = Student("wzh",20)
wzh.play_game()
"""
"""
# 类方法
# 	类方法在类中通过 @classmethod 定义，第一个参数为cls，代表类本身。
# 	类方法可以被类和实例对象调用。
# 	可以访问类属性。
# 	在不创建实例的情况下调用，通过类名直接调用，非常方便，适合一些和类整体相关的操作。

class Student:
    school = "atguigu"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def study(cls):
        print("study")
        print(cls.school)
        print(cls.__doc__)

zh = Student("wzh",20)
zh.study()

Student.study()
"""
"""
# 静态方法
# 	静态方法在类中通过 @staticmethod 定义
# 	不访问实例属性或类属性，只依赖于传入的参数
# 	可以通过类名或实例调用，但它不会访问类或实例的内部信息，更像是一个工具函数，只是为了方便组织代码，把它放在了类里面。
class Student:
    school = "atguigu"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def static_method():
        print("static method")

Student.static_method()
Student("zs",20).static_method()
"""
"""
# 在类外定义函数
def f1(self,x,y):
    print(x + y)
class C:
    f = f1

C().f(1,2)
"""
class Student:
    # def __new__(cls, *args, **kwargs):
    #     print("__new__")

    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

    def __del__(self):
        print("__del__")

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

s1 = Student("Zs", 20)
print(s1.age)
print(s1)
print(repr(s1))

ss = repr("print('hello world')") #这是一个字符串字面量
sss = "print('hello world')"
s2 = eval(ss)
s3 = eval(sss)
print(type(s2))
print(type(s3))

# 1）__new__()
# 对象实例化时第一个调用的方法。

# 2）__init__()
# 类的初始化方法。

# 3）__del__()
# 	对象的销毁器，定义了当对象被垃圾回收时的行为。使用 del xxx 时不会主动调用 __del__() ，除非此时引用计数==0。

# 4）__str__()
# 定义了对类的实例调用 str() 时的行为。

# 5）__repr__()
# 定义对类的实例调用 repr() 时的行为。 str() 和 repr() 最主要的差别在于目标用户。 repr() 的作用是产生机器可读的输出（大部分情况下，其输出可以作为有效的Python代码），而 str() 则产生人类可读的输出。

# 6）__getattribute__()
# 属性访问拦截器，定义了属性被访问前的操作。