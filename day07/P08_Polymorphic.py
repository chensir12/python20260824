"""
    该案例演示了多态
    同一个变量的多种不同形态
        在方法的参数中使用多态
        在方法的返回值中使用多态
        在定义的时候使用多态
"""

class Animal:
    def go(self):
        pass

class Dog(Animal):
    def go(self):
        print("跑")

class Fish(Animal):
    def go(self):
        print("游")

class Bird(Animal):
    def go(self):
        print("飞")

# 定义一个函数，让不同的动物动起来
def go(ani):
    ani.go()

go(Fish())
go(Bird())
go(Dog())

# 提供一个函数，可以创建不同的动物对象
def create_animal(flag):
    match flag:
        case 1:
            ani = Dog()
        case 2:
            ani = Fish()
        case _:
            ani = Bird()
    return ani

ani = create_animal(1)
print(type(ani))

class Student:
    pass

dog = Dog()
fish = Fish()
brid = Bird()
stu = Student()

list1 = [dog, fish, brid]
for ani in list1:
    ani.go()

