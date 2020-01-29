import cv2
import numpy as np
import brickpi3
import time
import datetime


stop_cascade = cv2.CascadeClassifier("stop_sign_default.xml") #für Stopschilderkennung
BP = brickpi3.BrickPi3() #für Motoansteuerung

def delay(duration_in_seconds):
    current_time = datetime.datetime.now()
    end_time = current_time + datetime.timedelta(0, duration_in_seconds)
    while current_time<end_time:
        current_time = datetime.datetime.now()

cap = cv2.VideoCapture(0) #Camera on
BP.set_motor_power(BP.PORT_B, 30) #Start driving
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #take image into grayscale
    stop = stop_cascade.detectMultiScale(gray, 3, 5)

    for(x,y,w,h) in stop: #draw a rectangle around the detected stop
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #color green, line width = 2
        font = cv2.FONT_HERSHEY_SIMPLEX #define font for text output
        cv2.putText(img, 'stop sign', (x-5, y-5), font, 1, (0, 255, 0), 3, cv2.LINE_AA) #write stopsign if detected
        print("Stopschild erkannt")
                
    if len(stop) != 0: #wenn Stopschild erkannt
        BP.set_motor_power(BP.PORT_B, 0) #anhalten
        print("Warte 3 Sekunden")
        delay(3)
        print("Weiterfahrt")
        BP.set_motor_power(BP.PORT_B, 30) #weiterfahren
        delay(4)
        BP.set_motor_power(BP.PORT_B, 0)
        
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #destroy whindows when pressing q
        break
cap.release()
cv2.destroyAllWindows()