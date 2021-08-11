#coding=utf-8
#该脚本用来校正和裁剪照片中的人脸

import cv2
import dlib
import math

path = "img/IMG_4.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#获取照片长宽
height,width = img.shape[:2]

#人脸分类器
detector = dlib.get_frontal_face_detector()
# 获取人脸检测器
predictor = dlib.shape_predictor(r"C:\Users\48162\AppData\Local\Programs\Python\Python39\Lib\site-packages\dlib-data\shape_predictor_68_face_landmarks.dat")

#获取人脸区域
dets = detector(gray, 1)
for face in dets:
    shape = predictor(img, face)  # 寻找人脸的68个标定点

#计算人脸中心坐标
eyecenter = ((shape.part(36).x + shape.part(45).x) * 1. / 2, (shape.part(36).y + shape.part(45).y) * 1. / 2)

#计算dx，dy
dx = shape.part(45).x - shape.part(36).x
dy = shape.part(45).y - shape.part(36).y

#计算角度
angle = math.atan2(dy, dx) * 180. / math.pi

#计算仿射矩阵
RotateMatrix = cv2.getRotationMatrix2D(eyecenter, angle, scale=1)

#转换照片
align_face = cv2.warpAffine(img, RotateMatrix, (width, height))

#重新计算人脸区域并剪裁
gray = cv2.cvtColor(align_face, cv2.COLOR_BGR2GRAY)
dets = detector(gray, 1)
for face in dets:
    shape = predictor(img, face)
facelength = shape.part(8).y - shape.part(24).y
facewidth = shape.part(16).x - shape.part(0).x
facecenter = ((shape.part(27).x + shape.part(8).x) * 1 / 2, (shape.part(27).y + shape.part(8).y) * 1 / 2)
x1, x2, y1, y2 = int(facecenter[0] - facewidth), int(facecenter[0] + facewidth),\
    int(facecenter[1] - 1.8 * facelength), int(facecenter[1] + 0.8 * facelength)
imgout = align_face[y1:y2, x1:x2]

cv2.imwrite("F:/Github/Image-Processing/img/CorrectedIMG_5.jpg", imgout)
height,width = imgout.shape[:2]  #获取原图像的水平方向尺寸和垂直方向尺寸。
res = cv2.resize(imgout,(width//2,height//2),interpolation=cv2.INTER_CUBIC)   #dsize=（2*width,2*height）
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()