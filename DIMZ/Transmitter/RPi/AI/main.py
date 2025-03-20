import configparser
import cv2
from ultralytics import YOLO

# Initialize the configparser
config = configparser.ConfigParser()
config.read('pathConfig.ini')

ncnn_model = YOLO(config['ncnn_paths']['model_path'])

#  Select the camera
cam = cv2.VideoCapture(0)
# while cam.isOpened():
#     pass

results = ncnn_model("https://ultralytics.com/images/bus.jpg")
