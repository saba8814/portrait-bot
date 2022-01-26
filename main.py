import cv2
from datetime import datetime


camera = cv2.VideoCapture(0)

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
        grey_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        invert_img=cv2.bitwise_not(grey_img)
        blur_img=cv2.GaussianBlur(invert_img, (105,105),0)
        invblur_img=cv2.bitwise_not(blur_img)
        sketch_img=cv2.divide(grey_img,invblur_img, scale=200)
        cv2.imwrite(img_name, sketch_img)
        print("{} written!".format(img_name))

camera.release()
cv2.destroyAllWindows()
    