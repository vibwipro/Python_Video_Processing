import cv2

cap = cv2.VideoCapture(0)
check, frame = cap.read ()
cv2.imshow("video", frame)

#### press '0' button to close window
cv2.waitKey(0)
cap.release()