"""
    晨测题
"""


# 创建一个迭代器类MyIterator，用于遍历一个给定列表的元素。实现__iter__和__next__方法。使用该迭代器类遍历列表[10, 20, 30, 40]，并打印每个元素。

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        x = self.data[self.index]
        self.index += 1
        return x

# 这个异常“没有报错”，是因为 for 循环内部“偷偷”捕获并处理了它。 StopIteration 不是程序员的“报错”，而是迭代器告诉循环“数据已发完”的标准信号
# mi = MyIterator([10, 20, 30, 40])
# for item in mi:
#     print(item)
it = iter(MyIterator([10, 20, 30, 40]))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
