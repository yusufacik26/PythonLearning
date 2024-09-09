
import cv2

import numpy as py

yakala = cv2.VideoCapture(0)

while(yakala.isOpened()):
    deger,kare = yakala.read()
    cv2.imshow("Ben",kare)
    a = cv2.waitKey(1)
    if a == 27:
        break


yakala.release()
cv2.destroyAllWindows()
