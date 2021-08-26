import torch
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time
import pyautogui
import sys
import os.path
sys.path.append('./deplacement')
import  deplacement
sys.path.append('./helpers')
from helpers.helpers import *
from helpers.mapDetection import *
sys.path.append('./ai')
from ai.ai import *
sys.path.append('./recolt')
from recolt.recolt import *
sys.path.append('./script')
from script.harvest import *
#CONSTANT
MODEL_PATH="./yolov5/runs/train/exp47/weights/best.pt"
IMG_SAMPLE="./assets/models/wheat/images/c2.png"
DIRECTORY_PATH="./assets/models/incarnam/images"

def main():
    model = loadModel(MODEL_PATH)
    #imgScanShow(model, IMG_SAMPLE)
    for filename in os.listdir(DIRECTORY_PATH):
        f = os.path.join(DIRECTORY_PATH, filename)
        imgScanShow(model, f)
        input("Press Enter to continue...")
    # harvestWheatOpti(model)
    # wereAmIonScreen()

if __name__ == "__main__":
    main()


