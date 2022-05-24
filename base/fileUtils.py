import re

def getFilePrefix(str):
    splits = str.split("/")
    name = ""
    if splits.__len__() > 0:
        name = splits[splits.__len__() - 1]
    return name.replace(getFileSuffix(name),"")

def getFileSuffix(str):
    findall = re.findall("[\.][^\.]*$", str)
    if findall.__len__() > 0:
        return findall[0]
    return ""

# 获取path 相对 parentPath的相对路径
def getRelativeName(path,parentPath):
    return path.replace(parentPath, "")
