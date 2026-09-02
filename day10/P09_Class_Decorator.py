"""
    该案例演示了类装饰器
"""
from math import sqrt


class MyClass:
    def __call__(self):
        print("callxxxxx")

mc = MyClass()
mc()

class DecoratorClass:
    def __init__(self,f):
        self.f = f

    def __call__(self, x):
        x = abs(x)
        return self.f(x)

@DecoratorClass
def func(x):
    return sqrt(x)

print(func(-4))

dc = DecoratorClass(func)
print(dc(-4))

