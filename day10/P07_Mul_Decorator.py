from math import sqrt


# 先将参数 求绝对值  再开方
def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

# 将字符串转换为整数的装饰器
def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

@get_integer
@get_abs
def func(x):
    return sqrt(x)

print(func("-4"))

# abs_inner = get_abs(func)
# int_inner = get_integer(abs_inner)
# print(int_inner("-4"))