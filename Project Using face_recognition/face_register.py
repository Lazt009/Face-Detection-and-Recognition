import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
# add = "http://25.98.196.191:8080/video"
# cap.open(add)

path = os.getcwd()
print(path)

index = 1
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    

    # Display the resulting frame
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    
    if key == ord('c'):
        name = path + "\\dataset\\mohit\\" + str(index) + ".jpg"
        #write image when pressed c
        cv2.imwrite(name, frame)  
        print("Frame registered "+ str(index) +".jpg" )
        index += 1
    elif key == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()