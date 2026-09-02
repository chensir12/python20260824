"""
    该案例演示了闭包
"""
def outer():
    a = 10
    b = 20
    def inner():
        return a + b
    return inner

inn = outer()
# print(inn())
# 返回的是一个元组，元组里面是每一个对象
cell_tup = inn.__closure__
print(cell_tup)
print(cell_tup[0].cell_contents)
print(cell_tup[1].cell_contents)