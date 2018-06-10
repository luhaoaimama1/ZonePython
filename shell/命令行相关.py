import sys
import os
import time

'''把内容推到命令行上 并且不换行'''
def print22():
    for i in range(10):
        print("\r====",i,end="")
        sys.stdout.flush()
        time.sleep(1)

'''获取命令行传入的参数'''
print(os.getcwd())
print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))
print22()

