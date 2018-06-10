from fold.core.DealFilesByFolder import *

'''
对处理的文件进行匹配后rename
'''
class FileCallback2(FileCallback):
#/Users/fuzhipeng/Desktop/文章/entity
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        with open(path,"r") as file:
            content=repr(file.readlines())
            if content.count(" class ")!=content.count("@Keep"):
                print("path:{2} **** class count:{0}\t @Keep count:{1}".format(content.count(" class "),content.count("@Keep"),path))

if __name__ == '__main__':
    selectFold(FilterCallback(),FileCallback2())

