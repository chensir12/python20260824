"""
    该案例演示了通过线程池的方式创建线程
"""
import concurrent.futures
import time


def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}:{word} \n",end="")
    time.sleep(0.5)
    return word

if __name__ == '__main__':
    word = list("idmmn!vnsme")
    print(word)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(func,"线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")
        print(future1.result())
        print(future2.result())
        print(future3.result())

    print("主线程","".join(word))






