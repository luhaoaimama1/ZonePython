# -*- coding: UTF-8 -*-
from crontab import CronTab
import os

'''
 M: 分（0-59）
 H：时（0-23）
 D：天（1-31）
 m: 月（1-12）
 d: 周（0-6） 0为星期日
 5 * * * * ：第五分钟
 */5 * * * * :每五分钟

使用范例：
crontabTasks2 = [
    CrontabTask("新任务2", "/Users/fuzhipeng/PycharmProjects/ZonePython/shell/crontab/pythontask2.py ", '* * * * *'),
]
addTask(crontabTasks2)  #添加任务

removeTask(crontabTasks2) #为了移除任务

'''

'''
任务实体类
以脚本path 为任务的key
所以 key 不会重复
重复就把以前的任务删除
'''
class CrontabTask:
    def __init__(self, comment, scriptPath, crontab):
        self.scriptPath = str(scriptPath).strip()
        self.comment = str(comment).strip()
        self.crontab = str(crontab).strip()


'''属性'''
envEncode = ''' LANG=it_IT.UTF-8'''
envPython3 = ''' /usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versions/3.6/bin/'''
python3 = '''python3'''
pySuffix = '''.py'''
# 过滤丢弃的task
invaildTasks = []


'''检查传入实体的正确性'''
def checkTaskVaild(crontabTasks):
    for task in crontabTasks:
        if len(task.scriptPath) == 0 or len(task.comment) == 0 or len(task.crontab) == 0:
            return False
    return True

'''添加任务 对于tasks之外的任务 仅仅检测脚本路径是否有效 失效移除'''
def addTask(crontabTasks):
    if not checkTaskVaild(crontabTasks):
        print("CrontabTask中 任何一个字段不可为空!")
        return
        __innerRealDealTask(crontabTasks, True)



def __innerRealDealTask(crontabTasks, isAdd):
    # 创建当前用户的crontab，当然也可以创建其他用户的，但得有足够权限
    my_user_cron = CronTab(user=True)
    # 迭代所有任务
    for task in my_user_cron:
        taskScriptPath = str(task)[(str(task).find(python3) + len(python3)):str(task).find(pySuffix)].strip() + pySuffix
        if not os.path.exists(taskScriptPath):
            # 删除 脚本不存在的 任务
            print("删除无效脚本(路径已失效)\tpath===>{}".format(taskScriptPath))
            invaildTasks.append(task)
        else:
            # 找到和现在重复的remove
            for key in crontabTasks:
                if taskScriptPath == key.scriptPath:
                    print("删除重复任务(因为新添加任务有此脚本)\tpath===>{}".format(taskScriptPath))
                    invaildTasks.append(task)
                    break
    '''移除无效任务'''
    if len(invaildTasks) != 0:
        for invaildTask in invaildTasks:
            my_user_cron.remove(invaildTask)
        my_user_cron.write()

    if isAdd:
        '''添加task里的任务'''
        my_user_cron = CronTab(user=True)
        for addTask in crontabTasks:
            newTask = my_user_cron.new(envEncode + envPython3 + python3 + ' ' + addTask.scriptPath)
            newTask.setall(addTask.crontab)
            newTask.set_comment(addTask.comment)
            print("添加任务中脚本===>{}".format(newTask))
    my_user_cron.write()  # 最后将crontab写入配置文件

def removeTask(crontabTasks):
    if not checkTaskVaild(crontabTasks):
        print("CrontabTask中 任何一个字段不可为空!")
        return
    __innerRealDealTask(crontabTasks, False)