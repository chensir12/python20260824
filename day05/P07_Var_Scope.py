"""
    该案例演示了变量的作用域
"""
aa = int(1.1) # 内建作用域 Builtin
a = 10 # 全局作用域 Global
def outer():
    a = 10 # 嵌套作用域（闭包） Enclosing
    def inner():
        print(a)  # 局部作用域 Local
    return inner
outer()()

# 注意：在python中，只有类、模块、函数才会引入新的作用域 if/while/for/try 不会引入新的作用域

aa = 10
if aa == 10:
    num1 = 20
    print(num1)

print(num1)
