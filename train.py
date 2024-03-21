'''
Author: maple 1910046133@qq.com
Date: 2024-03-20 19:23:29
LastEditors: maple
LastEditTime: 2024-03-21 16:56:04
Description: 
'''
from ultralytics import YOLO

# Load a model
# model = YOLO('./data/fall.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('./fall.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
model.train(data='./data/config.yaml', epochs=50, imgsz=640)