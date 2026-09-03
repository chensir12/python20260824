"""
    该案例演示了线程安全问题
"""
import threading
import time

"""
# 线程不安全情况演示
def func():
    global g_num
    for _ in range(10):
        # g_num += 1   ==> g_num = g_num + 1 ==>
        temp = g_num + 1
        time.sleep(0.1)
        g_num = temp
        print(f"当前线程{threading.current_thread().name}--->{g_num}")

if __name__ == '__main__':
    g_num = 0
    theads = [threading.Thread(target=func,name="线程"+str(i+1)) for i in range(3)]
    theads_ = [t.start() for t in theads]
    print("~~~~~~~~~~~theads",theads_)
    print(threading.current_thread().daemon)
    print(f"主线程:{g_num}")
"""

# 加锁解决线程安全问题
def func():
    global g_num
    for _ in range(10):
        # 加锁
        lock.acquire()
        temp = g_num + 1
        time.sleep(0.1)
        g_num = temp
        # 释放锁
        lock.release()
        print(f"当前线程{threading.current_thread().name}--->{g_num}")

if __name__ == "__main__":
    g_num = 0
    # 创建锁对象
    lock = threading.Lock()
    threads = [threading.Thread(target=func, name="线程" + str(i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(f"主线程:{g_num}")
