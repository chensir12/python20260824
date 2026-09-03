"""
    该案例演示了通过线程子类创建线程对象
"""
import threading
import time


class Worker123(threading.Thread):
    def run(self):
        flag = 0
        while True:
            print(threading.current_thread().name,f"{flag}"*5)
            flag = flag ^ 1
            time.sleep(0.5)

if __name__ == '__main__':
    t1 = Worker123(name="线程1")
    t1.start()
    t2 = Worker123(name="线程2")
    t2.start()
