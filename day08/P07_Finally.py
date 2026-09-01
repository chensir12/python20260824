"""
    该案例演示了finally
"""
"""
try:
    res = 1 / 0
    print(res)
except:
    print("发生了异常")
    print(a)
finally:
    print("~~~finally~~~")

print("~~~end~~~")
"""
"""
try:
    res = 10 / 0
    print(res)
except NameError:
    print("发生了异常")

print("~~~finally~~~")
print("~~~end~~~")
"""
# 面试题
# break   continue  return
def test_func():

    try:
        for i in range(10):
            if i == 5:
                return
            print(i)
    except:
        print("发生了异常")
    finally:
        print("~~~finally~~~")
# 无论如何都会执行finally
test_func()