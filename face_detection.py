

import cv2
import time

#import the image
test = cv2.imread('test.jpg')

gray_image = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Test Img',gray_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray_image,1.1,5)

print('Faces found: ',len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
    
cv2.imshow('Test Img',test)
cv2.waitKey(0)
cv2.destroyAllWindows()