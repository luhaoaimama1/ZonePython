from crontab import CronTab

# 创建当前用户的crontab，当然也可以创建其他用户的，但得有足够权限
my_user_cron=CronTab(user=True)

# 迭代所有任务
for item in my_user_cron:
    print(item)

'''定时执行pyhon脚本'''
task=my_user_cron.new(''' LANG=it_IT.UTF-8  /usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/fuzhipeng/PycharmProjects/ZonePython/shell/crontab/pythontask2.py''')
# my_user_cron.remove_all() #这里是移除用户的全部任务

'''
M: 分（0-59）
H：时（0-23）
D：天（1-31）
m: 月（1-12）
d: 周（0-6） 0为星期日
5 * * * * ：第五分钟
*/5 * * * * :每五分钟
'''
# 根据crontab 里的规则 可以自己设置
task.setall('* * * * *')

# 同时可以给任务设置comment，这样就可以根据comment查询，很方便
task.set_comment("测试定时")

# 任务的disable和enable， 默认enable
# task.enable(False)
# task.enable()

# 最后将crontab写入配置文件
my_user_cron.write()
#
# # 下面可通过命令查看，是否创建成功：
# # $ crontab -l