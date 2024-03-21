'''
Author: maple 1910046133@qq.com
Date: 2024-03-20 20:01:01
LastEditors: maple
LastEditTime: 2024-03-21 14:00:12
Description: 
'''
import os
import random

import shutil
from shutil import copy2
trainfiles = os.listdir(r"D:/bishe/code/yolov8-train/data/images/CCPD19")  #（图片文件夹）
num_train = len(trainfiles)
print("num_train: " + str(num_train) )
index_list = list(range(num_train))
print(index_list)
random.shuffle(index_list)  # 打乱顺序
num = 0
trainDir = r"D:/bishe/code/yolov8-train/data/train/images_1"   #（将图片文件夹中的7份放在这个文件夹下）
validDir = r"D:/bishe/code/yolov8-train/data/val/images_1"     #（将图片文件夹中的2份放在这个文件夹下）
detectDir = r"D:/bishe/code/yolov8-train/data/test/images_1"   #（将图片文件夹中的2份放在这个文件夹下）
for i in index_list:
    fileName = os.path.join(r"D:/bishe/code/yolov8-train/data/images/CCPD19", trainfiles[i])  #（图片文件夹）+图片名=图片地址
    if num < num_train*0.7:  # 7:1:2
        print(str(fileName))
        copy2(fileName, trainDir)
    elif num < num_train*0.9:
        print(str(fileName))
        copy2(fileName, validDir)
    else:
        print(str(fileName))
        copy2(fileName, detectDir)
    num += 1