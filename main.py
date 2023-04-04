# FaceDetection (https://github.com/hamdivazim/FaceDetection)
# This project is licnensed under the Apache License 2.0
# Do not claim as your own
#
# © Hamd Waseem 2023

import cv2

img_dir = input("Input directory of image to detect: ")

img = cv2.imread(img_dir)
cv2.imshow('Original Image', img)

height, width, channel = img.shape

print(f'Height: {height} , Width: {width} , Channel: {channel}')

blue, green, red = cv2.split(img)

cv2.imwrite('Blue.jpg', blue)
cv2.imwrite('Green.jpg', green)
cv2.imwrite('Red.jpg', red)

merged = cv2.merge((blue, green, red))
cv2.imwrite('Merged.jpg', merged)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(grey, 1.1, 4)

print(f'{len(faces)} faces detected.')

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_grey = grey[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_grey, 1.1, 2)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

cv2.imshow('Detected Faces', img)
