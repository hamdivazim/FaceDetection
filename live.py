# FaceDetection (https://github.com/hamdivazim/FaceDetection)
# This project is licnensed under the Apache License 2.0
# Do not claim as your own
#
# © Hamd Waseem 2023

import cv2
import time

cap = cv2.VideoCapture(0)

width = int(cap.get(3))
height = int(cap.get(4))

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))

font = cv2.FONT_HERSHEY_SIMPLEX

if cap.isOpened() == False:
    print('Camera footage not detected - try unplugging and plugging in your camera')

old_time = 0

while True:
    ret, frame = cap.read()

    if ret == True:
        img_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(img_grey, 1.1, 4)
        time_now = time.asctime(time.localtime(time.time()))

        cv2.putText(frame, time_now, (10, 450), font, 0.98, (0, 255, 0), 2, cv2.LINE_AA)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

            if time.time()-old_time > 30:
                cv2.imwrite(str(time.time()) + '_img.jpg', frame)
                old_time = time.time()

        if len(eye_cascade.detectMultiScale(img_grey, 1.1, 4)) > 0:
            out.write(frame)
            cv2.imshow('video_footage', frame)

        if cv2.waitKey(25) == ord('q'):
            break

cap.release()
out.release()

cv2.destroyAllWindows()


