# -*- coding=GBK -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# 高斯金字塔
def pyramid_image(image):
    level = 5  # 金字塔的层数
    temp = image.copy()  # 拷贝图像
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        dst = cv.GaussianBlur(dst, (13, 13), 0)  # 可以更改核大小
        cv.imshow("GaussianBlur Image" + str(i), dst)
        cv.imwrite("F:\\opencvxuexi\\filename%s.jpg"%i, dst)
        temp = dst.copy()
    return pyramid_images


src = cv.imread('F:\\opencvxuexi\\11.bmp')
cv.imshow("Source Image", src)
pyramid_image(src)
cv.waitKey(0)
cv.destroyAllWindows()