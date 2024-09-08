import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread("opencvlogo.png",0)
cv2.imshow("resimm",resim)
a = cv2.waitKey(0)

if a == 27:
    cv2.destroyWindow()
elif a == ord("s"):
    cv2.imwrite("opencv_S_tusu_ile_kaydetme.png",resim)   




