import os
from tool import PdfToImg
from tool import deal_white


def getfiles():
    # path_ = './crop_ph'
    path_ = './pdf'
    filenames = os.listdir(path_)
    for i in range(len(filenames)):
        filepath = os.path.join(os.path.realpath(path_), filenames[i])
        img_name = filenames[i].split('.')[0]
        PdfToImg.pdf2image1(filepath, './img_res', img_name)

    deal_white.file_save('./img_res', './pdf_res')



