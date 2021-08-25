import pyautogui
import time
import sys
sys.path.append('./helpers')
from helpers.helpers import *
from helpers.mapDetection import *
#fonction qui prend en p@ le tableau des ressources avec lequel on peut intéragier
# et va clicker dessus en fonction de ce qu'on veut recoler et le taux de confiance
def recolt(coord_array, ressource_id, confidence):
    cx = 0
    cy = 0
    if coord_array.size == 0:
        print("il n'y a rien à récolter")
    for array in coord_array:
        if (array[4] >= confidence and ressource_id == array[5]):
            print(array)
            print("Récolte d'une nouvelle ressource\n")
            cxprev = cx
            cyprev = cy
            cx = (array[0]/2+array[2]/2)/2
            cy = (array[1]/2+array[3]/2)/2
            s = calculateSleepTime(cx, cy, cxprev, cyprev)
            print("Position de la ressource : X : "+str(cx)+" Y : "+str(cy)+" \n")
            pyautogui.click(x=cx, y=cy)
            print("Le temps de récolte est de : "+str(s+3)+" s.\n")
            time.sleep(s+3)#temps de récolte+déplacement
            print("Fin de la récolte\n")

def recoltOnce(array, ressource_id, confidence):
    cx = 0
    cy = 0
    print(array)
    if array.size == 0:
        print("il n'y a rien à récolter")
    if (array[4] >= confidence and ressource_id == array[5]):
        print(array)
        print("Récolte d'une nouvelle ressource\n")
        cxprev = cx
        cyprev = cy
        cx = (array[0]/2+array[2]/2)/2
        cy = (array[1]/2+array[3]/2)/2
        s = calculateSleepTime(cx, cy, cxprev, cyprev)
        print("Position de la ressource : X : "+str(cx)+" Y : "+str(cy)+" \n")
        pyautogui.click(x=cx, y=cy)
        print("Le temps de récolte est de : "+str(s+3)+" s.\n")
        time.sleep(s+3)#temps de récolte+déplacement
        print("Fin de la récolte\n")
            
