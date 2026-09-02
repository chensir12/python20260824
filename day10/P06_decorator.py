"""
    该案例演示了装饰器
"""
from math import sqrt
"""
# 没有装饰器
from math import sqrt
def func(x):
    return sqrt(x)
# print(func(-4))
"""
"""
# 使用装饰器扩展函数的功能
from math import sqrt
def func(x):
    return sqrt(x)
# 定义装饰器函数  接收函数对象(被装饰的函数对象)作为参数
def decorator(f):
    # 定义内层函数 完成功能的扩展
    # 内函数的参数 和被修饰的函数的参数保持一致
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

inn = decorator(func)
print(inn(-4))
"""
"""

count= 0
# 开方函数
def func(x):
    return sqrt(x)

def power(x):
    return pow(x, 2)

def decorator(f,x):
    global count
    count += 1
    print(f"被装饰了{count}")
    x = abs(x)
    return f(x)

print(decorator(func,-4))
print(decorator(func,-4))
print(decorator(power,-4))
"""
# 装饰器语法糖

# 使用装饰器扩展 函数的功能
def decorator(f):
    count = 0
    def inner(x):
        nonlocal count
        count += 1
        print(f"当前函数被装饰{count}次")
        x = abs(x)
        return f(x)
    return inner

# 当我们使用 @decorator 前缀在 func 定义前，Python会自动将 func 作为参数传递给 decorator，然后将返回的 inner 函数替换掉原来的 func。
# 开方函数
@decorator
def func(x):
    return sqrt(x)

def power(x):
    return pow(x, 2)

inn1 = decorator(func)  #这个其实是调用了这个函数两次 是两个完全独立的内存空间（闭包）
print(inn1(-4))
print(inn1(-4))
# print(inn1(-4))
#
inn2 = decorator(power)
print(inn2(2))
print(inn2(2))

