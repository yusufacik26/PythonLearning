import cv2
import numpy as np

resim = cv2.imread("resim1.webp",0)

cv2.imshow("kurs",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

