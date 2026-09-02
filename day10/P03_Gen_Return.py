"""
    该案例演示了生成器函数的返回值
"""
def fibo(n):
    a, b ,count = 0, 1 , 1
    while count <= n:
        yield b
        a, b ,count = b, a + b ,count + 1

    return "done"

# f = fibo(5)
# print(type(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

try:
    f = fibo(10)
    while True:
        print(next(f))
except StopIteration as e:
    print (e)
