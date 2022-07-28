import numpy as np
import matplotlib.image as mpimg
import os
import time
import matplotlib.backends.backend_pdf

# 去除图片白边
from log.logger import Log


def resize_figure(img_path):
    img = mpimg.imread(img_path)
    ini_size = img.shape
    x = 0
    xx = img.shape[0]
    y = 0
    yy = img.shape[1]
    for channel in range(img.shape[2]):
        for i in np.arange(0, img.shape[0], 1):
            if img[i, :, channel].sum() != img.shape[1]:
                x = max(x, i)
                break
        for i in np.arange(img.shape[0] - 1, -1, -1):
            if img[i, :, channel].sum() != img.shape[1]:
                xx = min(xx, i)
                break
        for j in np.arange(0, img.shape[1], 1):
            if img[:, j, channel].sum() != img.shape[0]:
                y = max(y, j)
                break
        for j in np.arange(img.shape[1] - 1, -1, -1):
            if img[:, j, channel].sum() != img.shape[0]:
                yy = min(yy, j)
                break
    cutted_res = img[x - 5:xx + 5, y - 5:yy + 5, :]
    return cutted_res, ini_size, cutted_res.shape


# 获得某个文件夹下的所有的文件路径
def DFS_file_search(dict_name=None, out=None):
    # list.pop() list.append()这两个方法就可以实现栈维护功能
    if dict_name is None:  # 代表该根目录
        dict_name = './'
    stack = []
    result_txt = []
    stack.append(dict_name)
    while len(stack) != 0:  # 栈空代表所有目录均已完成访问
        temp_name = stack.pop()
        try:
            temp_name2 = os.listdir(temp_name)  # list ["","",...]
            for eve in temp_name2:
                stack.append(temp_name + "\\" + eve)  # 维持绝对路径的表达
        except NotADirectoryError:
            result_txt.append(temp_name)

    # 检查是不是图片格式
    if out is None:
        out = 'cutted'  # 默认的名字
    res = []
    for eve_path in result_txt:
        if eve_path.find('.') != -1 and eve_path.find(out) == -1:
            if eve_path.split('.')[-1] in ['png', 'PNG', 'jpg', 'JPG', 'eps', 'EPS']:
                res.append(eve_path)
    return res


def file_save(read_root_path, save_root_path):
    if not os.path.exists(save_root_path):
        os.mkdir(save_root_path)
    paths = DFS_file_search(read_root_path, save_root_path)

    Log.info('要处理的图片的路径为：{}'.format(paths))
    i = 1

    for path in paths:
        Log.info('开始处理 ' + path)
        t1 = time.time()
        cutted_figure, ini_size, final_size = resize_figure(path)
        mpimg.imsave('./' + save_root_path + "/" + str(i) + '.pdf', cutted_figure)
        Log.info('处理完毕：{}  耗时：{} 秒 处理前shape:{} 处理后shape:{}'.format(path, time.time() - t1, ini_size, final_size))
        i = i + 1
