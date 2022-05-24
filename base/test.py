# -*- coding: UTF-8 -*-
from base.fileUtils import getFilePrefix, getFileSuffix

if __name__ == '__main__':
    py = "/Users/fuzhipeng/PycharmProjects/ZonePythonNew/base/file/a.a.a.apk"
    print(py)
    print("getFilePrefix:{0}".format(getFilePrefix(py)))
    print("getFileSuffix:{0}".format(getFileSuffix(py)))
