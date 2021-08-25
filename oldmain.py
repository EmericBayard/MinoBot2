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
sys.path.append('./utils')
import  utils


# # results = mymodel(img)
# # results.print()
# # plt.imshow('yolo5s', np.squeeze(results.render()))
# # plt.show()

# # IMAGES_WHEAT_PATH = os.path.join('assets', 'models', 'wheat')
# # labels = ['wheat', 'gobbals']
# # number_imgs=20

# # while(True):
# #     image = pyautogui.screenshot()
    
# #     results = model(image)
# #     plt.imshow('YOLO', np.squeeze(results.render()))

# #     if cv2.waitKey(10) & 0xFF == ord('q'):
# #         break
# labels = ['wheat', 'gobbals']
# plt.switch_backend("tkagg")
# print(plt.get_backend())
# # for i in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
# #     # img = os.path.join('assets', 'models', 'wheat', 'images', 'c'+str(i)+'.png')
# #     # number_imgs = 20
# #     img = os.path.join('assets', 'models', 'wheat', 'images', 'c60.png')
# #     results = model(img)
# #     # plt.imshow(np.squeeze(results.render()))
# #     # plt.show() 
# img = os.path.join('assets', 'models', 'wheat', 'images', 'c60.png')
# results = model(img)
# # plt.imshow(np.squeeze(results.render()))
# # plt.show()
# # xmin, xmax, ymin, ymax, confidence, class
# print(results.xyxy) 
