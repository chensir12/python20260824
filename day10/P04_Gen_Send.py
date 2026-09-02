"""
    该案例演示了send向生成器发送数据
    需求:使用 send() 发送任务id，使生成器交替执行两个任务
"""
"""
.send() 的妙用在于它打破了“函数调用”的单向性，让生成器拥有了“记忆”和“响应外部指令”的能力。
如果你以后看 asyncio 源码或复杂的流式数据管道，你会发现到处都是这种“用 yield 挂起，用 send 唤醒”的黑魔法。😊
"""
def gen():
    task_id = 0
    int_value = 0
    char_value = 'A'
    while True:
        match task_id:
            case 0:
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield char_value
                char_value = chr(ord(char_value)+1)
            case _:
                # 返回None
                task_id = yield int_value
# f= gen()
# next(f) 等价于 f.send(None)
# next(f)
# print(next(f))
# print(next(f))
# print(next(f))

f = gen()
print(next(f))
print(f.send(1))

f = gen()
print(f.send(None))
print(f.send(1))
print(f.send(1))

f= gen()
print(f.send(None))
print(f.send(0))
print(f.send(0))
print(f.send(0))
print(f.send(0))
print(f.send(2))
print(f.send(2))


