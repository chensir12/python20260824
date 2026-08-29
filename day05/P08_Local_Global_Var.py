"""
    该案例演示局部变量以及全局变量
"""
def func_1():
    num1 = 10
    print(num1)

def func_2():
    num2 = 20
    print(num2)
    # print(num1)   访问不到
    print(num)
# 没有变量提升 是运行时动态查找
# func_2() # 会报错
num = 30
func_2()

var1 = 100
def func():
    # var1是全局变量，在func函数中可以访问
    # 在局部作用域中直接对全局变量不能修改，因为不能修改全局变量的指向
    # var1 += 10 # 报错 将var1当做局部变量处理，+=得先定义变量
    var1 = 200
    # print(var1)
    # var1 = var1 + 10
    # 如果在局部变量中就是要对全局变量做修改
    # global var1
    # var1 = 200
    print(f"var1局部{var1}")
func()
print(f"全局{var1}")

# nonlocal 也用作内部作用域修改外部作用域的变量的场景，不过此时外部作用域不是全局作用域而是嵌套作用域。
def outer():
    num1 = 10
    def inner():
        nonlocal num1
        num1 = 100
        print(f"局部{num1}")
    inner()
    print(f"嵌套{num1}")
outer()