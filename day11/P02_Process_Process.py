"""
    该案例演示了通过进程类创建进程对象
"""
import multiprocessing
import time


# 向文件中写入数据
def write_file():
    print(__name__,"~~~~~~~")
    with open('test.txt','w',encoding='utf-8') as f:
        while True:
            f.write("hello world111 \n")
            # 将缓冲区数据刷写到文件中
            f.flush()
            time.sleep(0.1)

# 从文件读取数据
def read_file():
    print(__name__,"~~~~~~~")
    with open('test.txt','r',encoding='utf-8') as f:
        while True:
            time.sleep(0.1)
            print(f.readline())

# 注意:在windows中通过multiprocessing.Process创建进程，__name__=="__main__"必须要加
if __name__ == '__main__':
    # 创建进程
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)
    print(p1.daemon)
    print(p2.daemon)
    # 启动进程
    p1.start()
    p2.start()

"""
1. Windows vs Linux 创建进程的根本差异
Linux / macOS（有 fork）：父进程调用 fork()，会克隆一份自己的内存镜像给子进程。子进程从“克隆那一刻”开始接着跑，知道自己是子进程，也知道该执行哪个函数。所以不强制要求 if __name__ == "__main__":。

Windows（没有 fork）：只能使用 spawn（产卵）方式。父进程启动子进程时，会开启一个崭新的 Python 解释器，然后让这个新解释器重新导入（import）你的 .py 文件。这相当于“把代码重新读一遍”。
"""
"""
1. 底层发生了什么（分步拆解）
第一步：父进程打包任务（Pickle 序列化）
当你执行 p.start() 时，父进程不是简单地说“去执行 worker”，而是做了以下动作：

它把 target=worker（函数对象）和 args=()（参数元组）打包（序列化）成一个二进制数据包。

这个包通过操作系统提供的管道（Pipe）或队列，发送给即将启动的子进程。

第二步：子进程启动（重新导入文件）
子进程启动了一个全新的 Python 解释器，开始从头执行你的 .py 文件。

当执行到 def worker(): 时，Python 解释器在子进程的内存里创建了一个名叫 worker 的函数对象。

执行到 if __name__ == "__main__": 时，由于子进程的 __name__ 不等于 "__main__"（而是 "__mp_main__" 或模块名），所以跳过了里面的 p.start() 代码。

此时：子进程只是加载了函数定义，并没有执行 worker()。

第三步：子进程接收指令并执行

子进程从管道中读取父进程发来的二进制数据包。

它反序列化（unpickle）这个包，从中还原出指令：“请调用 worker 函数，参数是 ()”。

子进程在自己的全局命名空间里查找名字叫 worker 的东西，找到了刚刚加载的函数对象，于是执行它。
"""
# *********
# 分布式或者是进程间的这种序列化和反序列化的前提是 反序列化的节点一定要在路径(例如classpath)上找到类定义,一般通过提前分发的jar包来完成