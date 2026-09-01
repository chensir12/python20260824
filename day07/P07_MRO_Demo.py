"""
    该案例演示了MRO的Demo
"""
"""
class Parent1:
    def __init__(self, value1):
        print("Initializing Parent1")
        self.value1 = value1

class Parent2:
    def __init__(self, value2):
        print("Initializing Parent2")
        self.value2 = value2

class Child(Parent1, Parent2):
    def __init__(self, value1, value2):
        print("Initializing Child")
        Parent1.__init__(self, value1)
        Parent2.__init__(self, value2)
c = Child("v1","v2")
print(c.value1)
print(c.value2)
"""
"""
class Parent1:
    def __init__(self, value1):
        print("Initializing Parent1")
        self.value1 = value1

class Parent2:
    def __init__(self, value2):
        print("Initializing Parent2")
        self.value2 = value2

class Child(Parent1, Parent2):
    def __init__(self, value1, value2):
        print("Initializing Child")
        # 调用 Parent1 的 __init__ 方法
        super().__init__(value1)
        # super().__init__(value2)
        # 调用 Parent2 的 __init__ 方法   Parent1 之后开始查找 MRO 链，调用下一个父类（即 Parent2）的 __init__ 方法，把 value2 传递进去。
        super(Parent1,self).__init__(value2)

child = Child("v1","v2")
print(child.value1)
print(child.value2)
"""

class GrandParent:
    def __init__(self):
        print("Initializing GrandParent")


class Parent1(GrandParent):
    def __init__(self):
        super().__init__()  # 方式2：父类也用 super()
        print("Initializing Parent1")

class Parent2(GrandParent):
    def __init__(self):
        super().__init__()  # 方式2：父类也用 super()
        print("Initializing Parent2")


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        pass
# super() 永远基于 self 的 MRO，而不是基于当前类。
print(Child.__mro__)
Child()


class Child(Parent1, Parent2):
    def __init__(self):
        # 方式2：仅需调用一次 super()，自动 MRO 流淌 处理所有父类/祖父类
        super(Child,self).__init__()

print(Child.__mro__)
Child()

"""
class Parent1:
    def __init__(self, value1, **kwargs):
        print("Initializing Parent1")
        super().__init__(**kwargs)
        self.value1 = value1

class Parent2:
    def __init__(self, value2, **kwargs):
        print("Initializing Parent2")
        super().__init__(**kwargs)
        self.value2 = value2

class Child(Parent2, Parent1):
    def __init__(self, value1, value2):
        print("Initializing Child")
        super().__init__(value1=value1, value2=value2)

child = Child("value from Parent1", "value from Parent2")
print(child.value1)  # 输出: value from Parent1
print(child.value2)  # 输出: value from Parent2
"""

# Python 社区为了解决复杂多继承参数传递而推崇的最佳实践约定。它的核心思想是 “各取所需，剩者上抛”