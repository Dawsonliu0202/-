#coding=utf-8
#这个demo主要用来测试dlib函数，例如标记人脸68个标定点

import cv2
import dlib

path = "img/IMG_4.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#人脸分类器
detector = dlib.get_frontal_face_detector()
# 获取人脸检测器
predictor = dlib.shape_predictor(r"C:\Users\48162\AppData\Local\Programs\Python\Python39\Lib\site-packages\dlib-data\shape_predictor_68_face_landmarks.dat")

dets = detector(gray, 1)
for face in dets:
    shape = predictor(img, face)  # 寻找人脸的68个标定点
    # 遍历所有点，打印出其坐标，并圈出来
    for pt in shape.parts():
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 4, (0, 0, 255), 2)

cv2.imwrite("F:/Github/Image-Processing/Code/Output2/img1.jpg", img)

height,width = img.shape[:2]  #获取原图像的水平方向尺寸和垂直方向尺寸。
res = cv2.resize(img,(width//2,height//2),interpolation=cv2.INTER_CUBIC)   #dsize=（2*width,2*height）
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
