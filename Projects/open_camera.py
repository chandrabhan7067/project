import cv2
cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    cv2.imshow('img',img)
    
    if cv2.waitKey() == 'q':
        break
    