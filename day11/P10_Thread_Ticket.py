"""
    该案例通过卖票案例演示了线程安全问题
"""
import threading
import time


def sale_ticket():
    global tick_num
    while True:
        lock.acquire()
        if tick_num <= 0:
            lock.release()
            break
        time.sleep(0.1)
        tick_num -= 1
        print(f"{threading.current_thread().name}卖了1张票，还剩{tick_num}张票")
        lock.release()
        time.sleep(0.1)


if __name__ == '__main__':
    tick_num = 100
    lock = threading.Lock()
    threads = [threading.Thread(target=sale_ticket,name="窗口" + str(i + 1)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print(f"主线程:{tick_num}")