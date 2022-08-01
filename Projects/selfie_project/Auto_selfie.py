import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    success,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # face = face_cascade.detectMultiScale(gray,1.3,5)

    # for x, y, w, h in face:
    #     cv2.rectangle(img , (x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow('img',gray)
    if cv2.waitKey(10) == ord('q'):
        break