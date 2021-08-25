import pyautogui
import time
import matplotlib
import matplotlib.pyplot as plt
import math 
#function that print cursor position
def wereAmIonScreen():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

#function that start MinoBot
def initMinobot():
    print("Starting", end="\n")
    for i in range (0,3):
        print(i, end="\n")
        time.sleep(1)
    print("Go !")

#function that change backend : exemple TkAgg
def changeBackend(backend_name):
    plt.switch_backend(backend_name)
    print("MatplotLibBackend is now : "+plt.get_backend())

#function qui calcule le temps d'attente pendant un déplacement
# au pire des cas 5S
def calculateSleepTime(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return (distance/2)*(1/190)

#function qui calcule le temps d'attente pendant un déplacement
# au pire des cas 5S
def calculateDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return (distance/2)
