import numpy as np
import cv2

# Kameradan görüntü alma
webcam = cv2.VideoCapture(0)

# While döngüsü başlatma
while(1):
    # Kameradan görüntü okuma
    _, imageFrame = webcam.read()

    # Görüntüyü BGR'den HSV'ye dönüştürme
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Sarı rengi için aralık belirleme ve maske oluşturma
    yellow_lower = np.array([20, 100, 100], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # Kırmızı rengi için aralık belirleme ve maske oluşturma
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Yeşil rengi için aralık belirleme ve maske oluşturma
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    # Mavi rengi için aralık belirleme ve maske oluşturma
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)



    # Görüntünün merkezine bir çarpı çizme
    height, width, _ = imageFrame.shape
    center_x, center_y = width // 2, height // 2

    # Çarpı çizme
    cv2.line(imageFrame, (center_x - 20, center_y), (center_x + 20, center_y), (255, 255, 255), 2)
    cv2.line(imageFrame, (center_x, center_y - 20), (center_x, center_y + 20), (255, 255, 255), 2)

    # Çarpının bulunduğu bölgeden renkleri tespit etme
    roi_size = 20  # Çarpı etrafındaki alanın boyutu
    roi = hsvFrame[center_y - roi_size:center_y + roi_size, center_x - roi_size:center_x + roi_size]

    # Renk tespiti ve ekranda gösterme
    def detect_color(roi, mask, color_name, color_val):
        mask_roi = mask[center_y - roi_size:center_y + roi_size, center_x - roi_size:center_x + roi_size]
        mean_val = np.mean(mask_roi)
        if mean_val > 0:
            cv2.putText(imageFrame, f"{color_name}", (center_x - 50, center_y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)

    # Çarpı bölgesindeki renkleri kontrol et
    detect_color(roi, red_mask, "Red", (0, 0, 255))
    detect_color(roi, green_mask, "Green", (0, 255, 0))
    detect_color(roi, blue_mask, "Blue", (255, 0, 0))
    detect_color(roi, yellow_mask, "Yellow", (0, 255, 255))

    # Programı sonlandırma
    cv2.imshow("Color Detection with Crosshair", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
