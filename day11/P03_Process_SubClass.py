"""
    该案例演示了通过继承Process创建进程对象
"""
import multiprocessing
import os


class Worker(multiprocessing.Process):
    def run(self):
        print(f"进程{os.getpid()},父进程{os.getppid()}")

if __name__ == '__main__':
    for i in range(3):
        p = Worker(name="进程"+str(i))
        p.start()