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
MODEL_PATH="./yolov5/runs/train/exp23/weights/rakib.pt"
IMG_SAMPLE="./assets/models/wheat/images/c1.png"

def main():
    model = loadModel(MODEL_PATH)
    harvestWheatOpti(model)
    # wereAmIonScreen()

if __name__ == "__main__":
    main()


