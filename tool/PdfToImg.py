import fitz
import re
import os


def pdf2image1(path, pic_path, name):

    checkIM = r"/Subtype(?= */Image)"  # 正则表达式
    pdf = fitz.open(path)
    lenXREF = pdf.xref_length()  # 最新fitz库是没有._getXrefLength()
    count = 1
    for i in range(1, lenXREF):
        text = pdf.xref_object(i)  # 最新fitz库是没有.getObjectString()
        isImage = re.search(checkIM, text)
        if not isImage:
            continue
        pix = fitz.Pixmap(pdf, i)
        if pix.size < 10000:  # 在这里添加一处判断一个循环
            continue  # 不符合阈值则跳过至下
        new_name = f"{name}.png"
        pix.save(os.path.join(pic_path, new_name))
        count += 1
