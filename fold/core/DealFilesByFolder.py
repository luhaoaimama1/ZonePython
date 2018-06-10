import os;

'''
使用说明：
对文件夹内所有的文件 过滤搜索 对找到的文件 进行处理！

example:

class FileCallback2(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        with open(path,"r") as file:
            content=repr(file.readlines())
            if content.count(" class ")!=content.count("@Keep"):
                print("path:{2} **** class count:{0}\t @Keep count:{1}".format(content.count(" class "),content.count("@Keep"),path))

selectFold(FilterCallback(),FileCallback2())

'''

# fold = '''/Users/fuzhipeng/Desktop/新手引导-互推 Asserts'''

def findFileByFold(fold, filterCallback, dealFileCallback):
    if not os.path.isdir(fold):
        pass
    for file in os.listdir(fold):
        if not file.endswith("DS_Store"):
            newFile = os.path.join(fold, file);
            if os.path.isdir(newFile):
                findFileByFold(newFile, filterCallback, dealFileCallback)
            if os.path.isfile(newFile) and filterCallback.filter(fold, file):
                dealFileCallback.dealFile(fold, file)

def selectFold(filter,dealFile):
    while True:
        fold = input("请输入源目录:")
        if os.path.exists(fold):
            findFileByFold(fold, filter, dealFile)
            break
        else:
            print("目录不存在!")

'''
提前过滤文件的
'''
class FilterCallback:
    def filter(self,fold,fileName):
        return True

'''
处理过滤后的文件的
'''
class FileCallback:
    def dealFile(self,fold,fileName):
        pass

