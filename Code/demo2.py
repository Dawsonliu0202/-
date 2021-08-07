#coding=utf-8
#这个demo主要用来测试CV2的一些函数，例如取灰度等

import cv2


filepath = "img/IMG_1.jpg"
img = cv2.imread(filepath)
# 转换灰色
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 显示图像
cv2.imshow("Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
