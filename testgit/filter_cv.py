# encoding:utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片

img = cv2.imread('F:\\opencvxuexi\\xinde.jpg')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 均值滤波
result1 = cv2.blur(source, (9, 9))  # 可以更改核的大小
# 显示图形
# titles = ['Source Image', 'Blur Image (3, 3)']
# images = [source, result]
# for i in range(2):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()


# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
cv2.imwrite("F:\\opencvxuexi\\mean_filter.jpg", result1)

# 中值滤波
result2 = cv2.medianBlur(img, 9)  # 可以更改核的大小

# 显示图像
# cv2.imshow("source img", img)
# cv2.imshow("medianBlur", result)
cv2.imwrite("F:\\opencvxuexi\\Median_filter.jpg", result2)

# 高斯滤波
result3 = cv2.GaussianBlur(source, (9, 9), 0)  # 可以更改核大小
cv2.imwrite("F:\\opencvxuexi\\Gaussian_Filte.jpg", result3)
# 显示图形
titles = ['Source Image',' Blur Image ',"medianBlur Image",'GaussianBlur Image ']
images = [source, result1,result2,result3,]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey (0)
cv2.destroyAllWindows()


