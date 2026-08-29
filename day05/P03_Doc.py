"""
    此案例演示了函数说明文档
"""
def adult(age):
    """该函数判断是否成年"""
    result = "未成年"[age >= 18:]
    return result
help(adult)