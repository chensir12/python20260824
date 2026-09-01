"""
    该案例演示了异常的传递
"""
try:
    try:
        try:
            print(1 / 0)
        except NameError as e:
            print("第一层try")
    except TypeError as e:
        print("第二层try")
except ZeroDivisionError as e:
    print("第三层try")


def m3():
    print(1/0)

def m2():
    m3()

def m1():
    m2()

m1()