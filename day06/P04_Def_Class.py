class Person:
    "人的类"
    # 类属性 --- 直接定义在类下的变量,当前这个类创建出来的所有实例共享
    home = "earth"
    # __init__ 是创建对象的时候，执行的方法
    def __init__(self, name, age):
        # self表示当前创建出来的对象 在__init__方法中，一般定义实例属性，并进行初始化

        # 实例属性 每个实例独有，互相隔离
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print("eating...")


# 类的操作

# 1.成员引用 类名.成员名
home = Person.home
eat = Person.eat # 获取一个函数对象

print(home)
print(eat)
print(Person.__doc__) # 获取类的说明文档

# 2.实例化 通过类这个模版创建对象的过程 类名()

# 当我们创建对象的时候，底层会自动调用__init__方法
p1 = Person("zs",20)
p2 = Person("ls",30)

print(p1.home)
print(p2.home)
print(p1.name,p1.age)
print(p2.name,p2.age)
p1.eat()
p2.eat()




