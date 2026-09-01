"""
    该案例演示了with代码块
"""
"""
Python中的with语句用于异常处理，封装了try except finally编码范式，
提供了一种简洁的方式来确保资源的正确获取和释放，同时处理可能发生的异常，提高了易用性。
使代码更清晰、更具可读性，简化了文件流等公共资源的管理
"""
"""
try:
    f = open("test.txt","w")
    f.write(a)
    f.close()
finally:
    print(f.closed)
"""
try:
    f = open("test.txt","w")
    try:
        f.write(a)
    except:
        print("error")
    finally:
        f.close()
finally:
    print(f.closed)

# with 的作用等效于 try finally 语句
try:
    with open("test.txt","w") as f:
        f.write("a")
finally:
    print(f.closed)

f = open("test.txt","w")
print(type(f))
