import cv2
import numpy as np
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.229.31.49', 22))  # Use the same port as on the Raspberry Pi
s.listen(5)

while True:
    conn, addr = s.accept()
    length = int(conn.recv(16))
    stringData = conn.recv(length)
    data = np.frombuffer(stringData, dtype='uint8')
    decimg = cv2.imdecode(data, 1)
    cv2.imshow('Video', decimg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
