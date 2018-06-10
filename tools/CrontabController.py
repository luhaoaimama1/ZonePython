from shell.crontab.core.CrontabCore import *

# 下面可通过命令查看，是否创建成功：
# $ crontab -l

crontabTasks2 = [
    CrontabTask("新任务2", "/Users/fuzhipeng/PycharmProjects/ZonePython/shell/crontab/pythontask2.py ", '* * * * *'),
]
removeTask(crontabTasks2)

# addTask(crontabTasks2)
