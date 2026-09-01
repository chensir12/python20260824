# Python是一门解释型语言，只有在程序运行后才会执行语法检查。所以，只有在运行或测试程序时，才会真正知道该程序能不能正常运行。
# Python有两种错误很容易辨认：语法错误和异常
"""
    该案例演示了else语句
"""
# 可选地将else放在所有except之后。如果try中代码没有发生异常，将执行 else 中的代码。
# 从执行效果上说，将代码放到else块和直接放到try块中是一样的。
# 将try正常执行完毕而没有引发任何异常后被执行的代码放到else中。提供了一种清晰的逻辑区分
"""
try:
    res = 1 / 0
except:
    print("发生异常了")
else:
    print(res)

print("~~~~~~end~~~~~~")
"""
"""
try:
    res = 1 / 0
    print(res)
except:
    print("发生异常了")

print("~~~~~~end~~~~~~")

try:
    res = 1 / 1
    print(res)
except:
    print("发生异常了")
else:
    print("这是else语句块")
"""
try:
    class Person:
        def __init__(self, name, age):
            self.name = name1
except:
    print("发生异常了")
else:
    print("else语句块")
    p = Person("zs")
