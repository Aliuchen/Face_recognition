# Face_recognition

#人脸识别  基于 MacOs + opencv + python 3.7 + face_recognition

#系统可以选择  Linux/mac  本样例测试于mac 终端


#准备工作 安装python 3.4以上   
 brew  install  python3 （mac)
 yum   install  python3  (linux)

#安装完毕 测试版本 
 python -V 

# 安装opencv - python   跨平台计算机视觉库  python版本
   pip install opencv-python
# 或者
  python3 -m pip install opencv-python
  (pytho3.4之后自带pip管理工具，如没有自行下载)

# 成功之后进入python命令行测试
  python3
  >> import cv2
  >>
  (成功)

# 安装face_recognition库   人脸识别基于face_recognition库。face_recognition基于dlib实现，用深度学习训练数据，模型准确率高达99.38%。
   pip install face_recognition

   （以上下载若是缓慢，可使用国内镜像 参考 https://zhuanlan.zhihu.com/p/125559588
 
# 进入python 命令行测试
  python3
  >> import face_recognition
  >>
  (成功)


# 环境搭建完成
