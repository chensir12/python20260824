"""
    该案例演示了match ...case
    给定月份，求该月有多少天
"""
from random import randint

month = randint(1,12)
print(f"当前月份是{month}")
"""
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("当前月有31天")
elif month == 4 or month == 6 or month == 9 or month == 11 :
    print("当前月有30天")
else:
    print("当前月有28或者29天")
"""
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 |12 :
        print("当前月有31天")
    case 4 | 6 | 9 | 11 :
        print("当前月有30天")
    case _:
        print("当前月有28或者29天")
