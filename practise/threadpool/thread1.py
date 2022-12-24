import time
from threading import Thread

def main(name = "python"):
    for i in range(10):
        print('hello ' + name + str(i))
        time.sleep(2)

thread_01 = Thread(target = main)
thread_01.start()

thread_02 = Thread(target = main, args = ("YZB",))
thread_02.start()

# t=Thread(target=func)

# 启动子线程
# t.start()
# 阻塞子线程，待子线程结束后，再往下执行
# t.join()
# 判断线程是否在执行状态，在执行返回True，否则返回False
# t.is_alive()
# t.isAlive()
# 设置线程是否随主线程退出而退出，默认为False
# t.daemon = True
# t.daemon = False
# 设置线程名
# t.name = "My-Thread"