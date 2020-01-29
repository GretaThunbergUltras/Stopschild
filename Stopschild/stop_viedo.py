import cv2
import numpy as np

stop_cascade = cv2.CascadeClassifier("stop_sign_default.xml")

cap = cv2.VideoCapture(0) #Camera on
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #take image into grayscale
    stop = stop_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in stop: #draw a rectangle around the detected stop
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #color green, line width = 2
        font = cv2.FONT_HERSHEY_SIMPLEX #define font for text output
        cv2.putText(img, 'stop sign', (x-5, y-5), font, 1, (0, 255, 0), 3, cv2.LINE_AA) #write stopsign if detected
        
        
        
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #destroy whindows when pressing q
        break
cap.release()
cv2.destroyAllWindows()