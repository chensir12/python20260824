"""
    该案例演示了继承
"""
# 子类不能继承父类的私有属性和私有方法，因为存在名称改写，但是可以通过改写后的名称直接访问父类的私有成员，不过，这种做法违背了封装原则，不建议使用
class Person:
    """人的类"""
    # 类属性
    home = "earth"
    def __init__(self,name):
        # 实例属性
        self.name = name

    # 实例方法
    def eat(self):
        print("eating")

class YellowRace(Person):
    color = "yellow"

class WhiteRace(Person):
    color = "white"

class BlackRace(Person):
    color = "black"

y = YellowRace("张三")
print(y.color,y.name,y.home)
y.eat()

w = WhiteRace("李四")
print(w.color,w.name,w.home)
w.eat()

b = BlackRace("王五")
print(b.color,b.name,b.home)
b.eat()
