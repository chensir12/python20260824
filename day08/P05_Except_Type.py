"""
    该案例演示了对不用类型异常进行不同的处理操作
"""
try:
    # 可能发生异常的代码
    print(1 / 0)
except NameError as e:
    print(e,"NameError")
except TypeError as e:
    print(e,"TypeError")
# except ZeroDivisionError as e:
#     print(e,"ZeroDivisionError")
# except (TypeError, ZeroDivisionError) as e:
#     print(e,"TypeError")
except:
    print("发生了异常")