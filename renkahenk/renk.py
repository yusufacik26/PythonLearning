from flask import Flask, jsonify, Response
import cv2
import numpy as np

app = Flask(__name__)

# Kamerayı başlatma
webcam = cv2.VideoCapture(0)

# Renk aralıklarını tanımlama
def detect_colors(imageFrame):
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Renk aralıkları ve maskeleri
    colors = {
        "yellow": ([20, 100, 100], [30, 255, 255]),
        "red": ([136, 87, 111], [180, 255, 255]),
        "green": ([25, 52, 72], [102, 255, 255]),
        "blue": ([94, 80, 2], [120, 255, 255])
    }
    
    detected_colors = {}

    for color_name, (lower, upper) in colors.items():
        lower_bound = np.array(lower, np.uint8)
        upper_bound = np.array(upper, np.uint8)
        mask = cv2.inRange(hsvFrame, lower_bound, upper_bound)
        if np.any(mask):  # Eğer maske içinde bir renk tespit edilirse
            detected_colors[color_name] = True
        else:
            detected_colors[color_name] = False

    return detected_colors

@app.route('/detect', methods=['GET'])
def detect():
    # Kameradan görüntü al
    success, imageFrame = webcam.read()
    if not success:
        return jsonify({'error': 'Kameradan görüntü alınamadı'}), 500

    # Renkleri tespit et
    detected_colors = detect_colors(imageFrame)

    return jsonify(detected_colors)

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            success, frame = webcam.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
