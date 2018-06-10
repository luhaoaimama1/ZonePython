import os;

'''
统计文字出现的次数   String.count
'''
while True:
    file = input("请输入源目录:")
    if os.path.isfile(file):
        break;
    else:
        print("不是文件 或者 不存在！")

quitStr=":wq"
print("退出标示="+quitStr)
while True:
    word = input("请输入匹配的字符:")
    if(word==quitStr):
        print("退出成功！")
        break
    try:
        with open(file, "r") as rf:
            content = rf.readlines()
            print("我出现的次数:", repr(content).strip().count(word))
    except:
        pass
