# Picture Processing

## 人脸识别照片动漫风格化工具    
     
### 主要技术路径
- OpenCV——对图片进行一系列操作
- 生成对抗网络，结合人脸检测、头发分割、人像分割等技术
- dlib——主要应用人脸识别技术
- PyQt——创建界面应用    
     
### 期待实现功能
- 可识别并突出照片人物进行风格化处理
- 识别照片人物表情并进行贴图
- 期待可通过微信小程序部署，增加用户量
- 其他功能以待完善    
     
### 已实现功能
**人像识别及预处理**    

>**实例一**    
首先人脸识别，标定关键点

![1](https://pic.imgdb.cn/item/611387635132923bf859216f.jpg)

> 然后根据关键点计算人眼连线与水平夹角，并将照片进行旋转

![2](https://pic.imgdb.cn/item/611387635132923bf8592194.jpg)

> 重新计算人脸区域并按比例剪裁

![3](https://pic.imgdb.cn/item/611387635132923bf85921a1.jpg)

> 预处理之后得到的照片

![4](https://pic.imgdb.cn/item/611387635132923bf85921ae.jpg)

**照片动漫风格化处理**    

>**实例二**    
转换前效果：

![转换前1](https://pic.imgdb.cn/item/6113869a5132923bf8578e2c.jpg)
>转换后效果：

![转换后1](https://pic.imgdb.cn/item/6113869a5132923bf8578e35.jpg)


     
### 参考案例
1. [一款入门级别人脸、视频、文字检测项目](https://github.com/vipstone/faceai)
2. [使用openCV+pyqt5实现照片卡通化](https://github.com/starsD/Cartoonish-pic)


