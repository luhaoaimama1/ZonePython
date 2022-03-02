# -*- coding: UTF-8 -*-
import os;

from subprocess import Popen,PIPE

'''
　这两个都是用当前进程来调用，也就是说它们都是阻塞式的。
'''
# os.system("ls")
# os.popen("ls").readlines()

'''
运行原理会在当前进程下面产生子进程。
'''
import subprocess
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line),
retval = p.wait()