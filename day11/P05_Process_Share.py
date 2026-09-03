"""
    该案例演示了进程之间数据的共享
"""
import multiprocessing
import os
import random
import time

"""
# 进程间不共享全局变量
# 默认情况下 进程之间内存隔离，数据不能共享
# 向list1中添加10个元素
def func(list1):
    for i in range(10):
        time.sleep(1)
        list1.append(i)
        print(os.getpid(),list1)

if __name__ == '__main__':
    list1 = []
    p1 = multiprocessing.Process(target=func,args=(list1,))
    p2 = multiprocessing.Process(target=func,args=(list1,))
    p1.start()
    p2.start()

    # join([timeout])：阻塞主进程，直到子进程结束或超时。timeout参数可选，意为阻塞多少秒。
    # p1.join()
    # p2.join()
    print("主进程:",os.getpid(),list1)
"""

# 通过Queue 实现进程之间的数据的共享
# 间隔随机时间向queue中放入随机数
def func1(queue):
    while True:
        rand_num = random.randint(1, 50)
        queue.put(rand_num)
        print(f"进程{os.getpid()}向队列中放入了元素{rand_num}")
        time.sleep(0.5)

# 从queue中取出数据
def func2(queue):
    while True:
        num = queue.get()
        print(f"进程{os.getpid()}从队列中取出了元素{num}")
        time.sleep(0.5)

if __name__ == '__main__':
    # queue = multiprocessing.Queue()
    # p1 = multiprocessing.Process(target=func1,args=(queue,))
    # p2 = multiprocessing.Process(target=func2,args=(queue,))
    #
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
#     注意：multiprocessing.Queue存在兼容性问题，如果要使用进程池，可以使用Mananger().Queue
    queue = multiprocessing.Manager().Queue()
    # queue = multiprocessing.Queue()
    pool = multiprocessing.Pool(2)
    pool.apply_async(func=func1,args=(queue,))
    pool.apply_async(func=func2,args=(queue,))

    pool.close()
    pool.join()
