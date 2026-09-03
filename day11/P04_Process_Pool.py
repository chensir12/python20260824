"""
    该案例演示了通过进程池的方式创建进程对象
"""
import multiprocessing
import os
import time


def func():
    for i in range(10):
        print(os.getpid(),i)
        time.sleep(0.5)

if __name__ == '__main__':
    num_process = 5
    pools = multiprocessing.Pool(num_process)

    for _ in range(num_process):
        # apply(func[, args[, kwds]])：
        # 使用 args 参数以及 kwds 命名参数同步调用 func , 在返回结果前阻塞。另外 func 只会在一个进程池中的一个工作进程中执行。
        # pools.apply(func)
        # 非阻塞式
        pools.apply_async(func=func)
    pools.close()
    # 从3.8版本后，进程池的进程默认是守护进程，所以需join()确保主进程等待。
    pools.join()

    print("~~~end~~~")