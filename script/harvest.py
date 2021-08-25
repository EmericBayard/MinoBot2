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


def harvestWheat(model):
    initMinobot()
    mapScan(model)
    array_coord = getCoordFromMap(model)
    recolt(array_coord, 0, 0.6)

def harvestWheatOpti(model):
    initMinobot()
    mapScan(model)
    array_coord = getCoordFromMap(model)
    while (array_coord.size):
        recoltOnce(array_coord[0], 0, 0.6)
        array_coord = getCoordFromMap(model)