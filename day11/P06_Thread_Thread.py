"""
    该案例演示了通过Thread类创建线程对象
"""
import threading
import time

import time
import threading
"""
# 两个线程分别交替打印 00000 和 11111 操作的都是各自的变量
def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f"{flag}" * 5)
        flag = flag ^ 1  # 替换0和1
        time.sleep(0.5)

if __name__ == '__main__':
    t1  = threading.Thread(target=func,name="t1")
    t2  = threading.Thread(target=func,name="t2")
    t1.start()
    t2.start()

    print("~~~主线程~~~")
"""

# 交替打印 00000 和 11111 两线程操作一个共同的全局变量
def func():
    # 存在线程安全问题
    global flag
    while True:
        print(threading.current_thread().name,f"{flag}"*5)
        flag += 1
        time.sleep(0.5)

if __name__ == '__main__':
    flag = 0
    t1 = threading.Thread(target=func,name="t1")
    t2 = threading.Thread(target=func,name="t2")
    t1.start()
    time.sleep(1)
    t2.start()

    print("~~~主线程~~~")