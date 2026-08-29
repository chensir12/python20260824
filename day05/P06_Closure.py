"""
该案例演示了闭包
闭包必须同时满足以下 3个核心条件：
1.函数嵌套（在一个函数内部定义另一个函数）。
2.内部函数引用了外部函数的局部变量（即自由变量）。
3.外部函数将内部函数作为返回值返回（或将内部函数传递出去，使其生命周期延长）。
"""
# 需求：想在一个函数的函数体中，访问另一个函数体中定义的变量
"""
def func_a():
    print("start~a")
    num = 10
    func_b(num)
    print("end~a")

def func_b(nn):
    print("start~b")
    print(nn)
    print("end~b")

func_a()
"""
# 函数嵌套定义
def outer():
    num = 10
    def inner():
        print(num)
    return inner
outer()()
# 获取内部函数对象
inn = outer()
# 调用内函数
inn()
