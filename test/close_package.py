from datetime import datetime
import time
def timer(func):
    def real(*args,**kwargs):
        bt = datetime.now()
        a = func(*args,**kwargs)
        et = datetime.now()
        print(f'函数耗时：{et-bt}')
        return a
    return real


@timer
def add():
    sum = 0
    for i in range(10000):
        sum = sum + i
    time.sleep(2)
add()