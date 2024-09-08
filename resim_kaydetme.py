import cv2
import numpy as np

resim = cv2.imread("opencvlogo.png",0)

cv2.imshow("kurs",resim)
cv2.imwrite("opencvlogosugri.png",resim,)


