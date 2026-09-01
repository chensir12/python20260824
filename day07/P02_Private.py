"""
    该案例演示了封装
"""
"""
# 将变量和函数写入类中的操作即为封装，即类中封装了属性和方法。
# 通过封装，我们可以将一些细节隐藏起来（私有），只暴露出必要的接口供调用者使用。
# 私有属性
class Girl:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    # 获取__age属性的值
    def get_age(self):
        if self.__age >= 18:
            return 18
        else:
            return self.__age

    # 设置__age属性的值
    def set_age(self, age):
        self.__age = age - 2
zs = Girl("zs",30)
print(zs.name)
# print(zs.__age)
# 1）单下划线：非公开API 不具备强制力
# 2）双下划线：名称改写 类内部可以通过 __x 访问 其他地方无法访问或只能通过 _类名__x 访问
# print(zs._Girl__age)

print(zs.get_age())
zs.set_age(30)
print(zs.get_age())
"""
"""
# 私有方法
class Person:
    # 定义私有方法
    def __private_method(self):
        print("private method")

    # 定义实例方法,调用私有方法
    def do_something(self):
        self.__private_method()
p = Person()
p.do_something()
p._Person__private_method()
# p.__private_method() #报错
"""
class Girl:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    @property #将方法转换成属性的形势
    def eat(self):
        print("eating")
    # 获取__age属性的值
    @property #只读属性
    def age(self):
        if self.__age >= 18:
            return 18
        else:
            return self.__age

    # 设置__age属性的值
    @age.setter #读写属性
    def age(self, age):
        self.__age = age - 2


zs = Girl("zs",30)
zs.eat
zs.age = 18
print(zs.age)

