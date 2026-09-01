"""
    该案例演示了异常的抛出 Raise,Assert
"""
"""
def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        # 抛出异常
        raise TypeError("参数必须传递整数")

try:
    print(add(1,"2"))
except TypeError as e:
    print(e)

class MyException(Exception):
    pass
"""
"""
def welcome(name,age):
    if age >= 0 and age <= 200:
        print("Hello",name,"!",age)
    else:
        raise MyException("年龄必须在0~200之间")

welcome("Zs",200)
"""
# assert断言   assert 表达式 [,异常描述]
def add(a,b):
    assert isinstance(a,int) and isinstance(b,int), "参数必须传递整数"
    return a + b
print(add(10,"20"))


