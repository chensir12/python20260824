"""
    该案例演示了装饰器参数
"""
from math import sqrt


def times(n):
    def get_absolute(f):
        def inner(x):
            x = abs(x)
            for i in range(n):
                x = f(x)
            return x
        return inner
    return get_absolute

@times(n=2)
def func(x):
    """开根号"""
    return sqrt(x)

print(func(-16))
print(times(2)(func)(-16))

