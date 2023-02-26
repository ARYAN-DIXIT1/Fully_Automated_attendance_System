import cv2
import numpy as np
import face_recognition

img_ayush=face_recognition.load_image_file('ayush_train.jpeg')
img_ayush=cv2.cvtColor(img_ayush,cv2.COLOR_BGR2RGB)

img_ayush_test=face_recognition.load_image_file('ayush_test.jpeg')
img_ayush_test=cv2.cvtColor(img_ayush_test,cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_locations(img_ayush)[0]
encodeAyush=face_recognition.face_encodings(img_ayush)[0]
cv2.rectangle(img_ayush,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2 )
# print(faceloc)
 

faceloc_test=face_recognition.face_locations(img_ayush_test)[0]
encodeAyush_test=face_recognition.face_encodings(img_ayush_test)[0]
cv2.rectangle(img_ayush_test,(faceloc_test[3],faceloc_test[0]),(faceloc_test[1],faceloc_test[2]),(255,0,255),2 )
# print(faceloc)

results=face_recognition.compare_faces([encodeAyush],encodeAyush_test)
faceDis=face_recognition.face_distance([encodeAyush],encodeAyush_test)
print(results,faceDis)
cv2.putText(img_ayush_test,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('ayush_train',img_ayush)
cv2.imshow('ayush_test',img_ayush_test)
cv2.waitKey(0)
