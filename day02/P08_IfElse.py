"""
    该案例演示了双分支
    余额随机，商品价格50。
    	若余额小于50则提示“余额不足，请充值”。
    	否则提示消费成功。
    最后打印“欢迎下次光临”。
"""
from random import randint
price = 50
balance = randint(1,100)
print(f"当前余额：{balance}")
if balance < price:
    print("余额不足，请充值")
else:
    print("消费成功")

print("欢迎下次光临")


