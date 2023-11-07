import cv2
import numpy as np
import socket

cap = cv2.VideoCapture(0)  # Access the USB camera (adjust the index if necessary)

while True:
    ret, frame = cap.read()
    # Convert the frame to bytes
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    _, frame = cv2.imencode('.jpg', frame, encode_param)
    data = np.array(frame)
    stringData = data.tostring()

    # Create a socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('YOUR_LAPTOP_IP', YOUR_PORT))  # Replace with your laptop's IP and a chosen port

    # Send the frame data
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
    s.close()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
