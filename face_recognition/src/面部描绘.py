'''
本样例测试 需要提前准备好人物照片，face_recognition.load_image_file  提供相对路径
'''
from PIL import Image, ImageDraw

import face_recognition

#将jpg文件加载到numpy数组中
image = face_recognition.load_image_file("/Users/liuchen/Desktop/opencv/unknown.jpg")

#找出图片中所有人的面部特征
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

#创建一个PIL imagedraw对象，这样我们可以在图片上绘制
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    #打印图像中每个面部特征的位置
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

     #让我们用线条描绘出图像中的每个面部特征!
    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)

# 展示图片
pil_image.show()

