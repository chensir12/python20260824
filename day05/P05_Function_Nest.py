"""
    该案例演示了函数的嵌套调用
"""

def func_a():
    print("~~~A开始执行~~~")
    func_b()
    print("~~~A执行结束~~~")
def func_b():
    print("~~~B开始执行~~~")
    print("~~~B执行结束~~~")
func_a()