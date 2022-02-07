import cv2
import linedraw
from datetime import datetime


camera = cv2.VideoCapture(0)
img_name =""
if not camera.isOpened():
    raise IOError("Webcam not detected")

while True:
    ret, frame = camera.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    cv2.imshow('Camera', frame)
    c = cv2.waitKey(1)
    if c == 27:
        print("Escape hit, closing...")
        break
    if c == 32:
        img_name = datetime.now().strftime("%d-%m-%Y-%H%M%S")+".png"
        #resized_image = cv2.resize(frame, (512, 512)) 
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

lines = linedraw.sketch(img_name)
linedraw.visualize(lines) 
camera.release()
cv2.destroyAllWindows()
    