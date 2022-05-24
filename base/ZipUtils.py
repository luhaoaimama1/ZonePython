import os
import zipfile
from base.fileUtils import getFilePrefix
from fold.core.DealFilesByFolder import FileCallback, FilterCallback, findFileByFold


def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name)
    for names in zip_file.namelist():
        name = getFilePrefix(file_name)
        zip_file.extract(names, name)
    zip_file.close()


def zip(fold, output_file_name):
    path = os.path.join(fold, output_file_name)
    if os.path.exists(path):
        os.remove(path)

    zip_file = zipfile.ZipFile(path, "w")

    class FileCallbackInner(FileCallback):
        def dealFile(self, foldInner, fileName):
            path_inner = os.path.join(foldInner, fileName)
            # print("{0}->{1}".format(path_inner, path_inner.replace(fold, "")))
            zip_file.write(path_inner, path_inner.replace(fold, ""))

    findFileByFold(fold, FilterCallback(), FileCallbackInner())
    zip_file.close()


def add_file_to_zip(file, zipPath):
    if os.path.exists(file):
        zip_file = zipfile.ZipFile(zipPath, "a")
        os.path.basename(file)
        zip_file.write(file, os.path.basename(file))
        zip_file.close()
