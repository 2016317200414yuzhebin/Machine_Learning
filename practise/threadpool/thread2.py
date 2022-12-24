import time
from threading import Thread

class MyThread(Thread): # 继承了父类Thread的属性
    def __init__(self, name = "Python"): # 此处子类做了初始化，如果此时不调用super初始化父类构造函数则不会自动继承父类属性
        super().__init__()
        self.name = name
    
    def run(self):
        for i in range(10):
            print("hello " + self.name + " " + str(i))
            time.sleep(1)

if __name__ == '__main__':
    thread_01 = MyThread()
    thread_02 = MyThread("YZB")
    thread_01.start()
    thread_02.start()
