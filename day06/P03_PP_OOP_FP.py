"""
    面向过程、面向对象、面向函数编程对比
"""
"""
# 面向过程   以「步骤 / 流程」为核心	拆解问题为 “步骤 + 数据”，按顺序执行	关注 “怎么做”（How）
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(f"10和20相加的结果是{add(10,20)}")
print(f"10和20相减的结果是{sub(10,20)}")
print(f"10和20相乘的结果是{mul(10,20)}")
print(f"10和20相除的结果是{div(10,20)}")
"""
# 面向对象  面向对象	以「对象 / 实体」为核心	封装数据与行为，通过交互解决问题	关注 “谁来做”（Who）
class Calculator:
    def add(self,a, b):
        return a + b

    def sub(self,a, b):
        return a - b

    def mul(self,a, b):
        return a * b

    def div(self,a, b):
        return a / b

zsC = Calculator()
print(zsC.add(10,20))
print(zsC.sub(10,20))
print(zsC.mul(10,20))
print(zsC.div(10,20))

# 面向函数式编程   以「纯函数 / 数据转换」为核心	用函数组合实现逻辑，避免状态变化	关注 “做什么”（What）
# 函数是一等公民    函数可以作为参数进行传递   函数也可以作为返回值进行返回
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calculator(a,b,func):
    return func(a,b)

print(calculator(10, 20, add))
print(calculator(10, 20, sub))
print(calculator(10, 20, mul))
print(calculator(10, 20, div))