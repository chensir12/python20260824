"""
    该案例演示了生成器的创建
"""
from typing import Iterator

# 生成器就是一种迭代器
"""
from collections.abc import Iterator

# 方式1 推导式
gen = (i for i in range(5))
print(type(gen))
print(isinstance(gen,Iterator))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

# 提供函数生成斐波那契数列
def fibo(n):
    a, b,i = 0,1,1
    while i <= n:
        print(b)
        a, b ,i = b, a+b,i+1
fibo(10)

# 方式2 使用函数创建生成器对象
def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
print(type(fibo))
f = fibo()
print(type(f))
print(isinstance(f,Iterator)) #生成器就是一种迭代器
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
