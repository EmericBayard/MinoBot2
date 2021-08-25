import torch
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time
import pyautogui
import sys
sys.path.append('./helpers')
from helpers.helpers import *
from helpers.mapDetection import *

#load my pretrained model
def loadModel(path):
    return torch.hub.load('ultralytics/yolov5', 'custom', path=path, force_reload=True)


#Scan la map pour renvoyer le contenu detecté par le moodel
def mapScan(model):
    map = pyautogui.screenshot()
    return model(map)

#scan une image passé en parametre et renvoie les objets détectés
def imgScan(model, img_path):
    return model(img_path)

#montre les box tracé par le model
def imgScanShow(model, img_path):
    changeBackend("tkagg")
    results = imgScan(model, img_path)
    results.show()

#renvoie les coordonnées des box que le modele à tracé xmin, xmax, ymin, ymax, confidence, class
#renvoie sous forme de tableau
def getCoordFromImg(model, img_path):
    results = imgScan(model, img_path)
    b = results.xyxy[0]
    a = b.numpy()
    return a

#renvoie les coordonnées des box que le modele à tracé xmin, xmax, ymin, ymax, confidence, class
#renvoie sous forme de tableau
#en fonction de la vue pyautogu
def getCoordFromMap(model):
    map = pyautogui.screenshot()
    results = imgScan(model, map)
    b = results.xyxy[0]
    a = b.numpy()
    return a

