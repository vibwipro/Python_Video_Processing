import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

camera_port = 0
gimage = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)


while True:
    _, frame = gimage.read()
    detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gryimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = detect.detectMultiScale(gryimg, 1.25, 3)

    ## It will add square around face.
    for (x, y, w, h) in face:
        cv2.rectangle( frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    ### press 'Esc' key to close
    if key == 27:
        break


