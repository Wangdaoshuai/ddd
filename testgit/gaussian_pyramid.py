# -*- coding=GBK -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# ��˹������
def pyramid_image(image):
    level = 5  # �������Ĳ���
    temp = image.copy()  # ����ͼ��
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        dst = cv.GaussianBlur(dst, (13, 13), 0)  # ���Ը��ĺ˴�С
        cv.imshow("GaussianBlur Image" + str(i), dst)
        cv.imwrite("F:\\opencvxuexi\\filename%s.jpg"%i, dst)
        temp = dst.copy()
    return pyramid_images


src = cv.imread('F:\\opencvxuexi\\11.bmp')
cv.imshow("Source Image", src)
pyramid_image(src)
cv.waitKey(0)
cv.destroyAllWindows()