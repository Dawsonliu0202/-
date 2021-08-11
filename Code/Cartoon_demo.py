#coding=utf-8
#这个demo主要用来测试照片卡通化
import os
import cv2

#高斯双边/均值漂移滤波器
def bilateral_filter(img, filter):
    if filter == 0:
        # 高斯双边滤波
        dst = cv2.bilateralFilter(src=img, d=7, sigmaColor=100, sigmaSpace=15)
    elif filter == 1:
        # 均值漂移滤波
        dst = cv2.pyrMeanShiftFiltering(src=img, sp=15, sr=20)
    return dst


#取灰度
def get_gray(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img


#中值滤波器
def median_fiflter(img, size=9):
    median_img = cv2.medianBlur(img, size)
    return median_img


#取边缘
def get_edge(img, blocksize=5):
    edge_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C=2)
    edge_img = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2RGB)
    return edge_img


#下采样
def pyramid(img, level=2):
    temp = img.copy()
    pyramid_images = []
    for i in range(level):
        pyramid_img = cv2.pyrDown(temp)
        pyramid_images.append(pyramid_img)
        temp = pyramid_img.copy()
    return pyramid_images[-1]


#上采样
def pyrUp(img, level=2):
    temp = img.copy()
    for i in range(level):
        #
        # for k in range(1):
        #     temp = bilateral_filter(temp, self.parameters['bilateral_filter'])
        temp = cv2.pyrUp(temp)
    return temp


if __name__ == '__main__':

    #读取照片文件
    path = "F:/Github/Image-Processing/img/IMG_5.jpg"
    outpath = "F:/Github/Image-Processing/img/"
    
    img = cv2.imread(path)

    #下采样
    pyramid_img = pyramid(img)

    #上采样
    pyrup_img = pyrUp(pyramid_img)

    #均值漂移滤波
    dst = bilateral_filter(pyrup_img, 1)

    #取灰度
    gray_img = get_gray(dst)

    #中值滤波
    median_img = median_fiflter(gray_img)

    #边缘检测
    edge_img = get_edge(median_img)

    #图像合并
    cartoon_img = cv2.bitwise_and(dst, edge_img)

    #储存图片
    cv2.imwrite(outpath + "OUTIMG_5.jpg", cartoon_img)

    height,width = img.shape[:2]  #获取原图像的水平方向尺寸和垂直方向尺寸。
    res = cv2.resize(cartoon_img,(width//2,height//2),interpolation=cv2.INTER_CUBIC)   #dsize=（2*width,2*height）
    cv2.imshow('res',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()