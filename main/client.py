import datetime

from log.logger import Log
from tool import get_dir_file
import os


def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)


if __name__ == '__main__':
    del_files('./img_res')
    Log.info("运行前先删除img_res文件夹下的文件")
    del_files('./pdf_res')
    Log.info("运行前先删除pdf_res文件夹下的文件")
    get_dir_file.getfiles()
