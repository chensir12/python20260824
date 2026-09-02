from collections.abc import Iterator


class MyTest:
    def __iter__(self):
        return self
    def __next__(self):
        pass

mt = MyTest()
print(isinstance(mt,Iterator))