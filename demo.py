import cv2
import face_recognition
import numpy as np
import os

img_jack = cv2.imread('Data/Jack_Ma1.jpg')
img_jack = cv2.resize(img_jack, (800, 500))
img_jack_test = cv2.imread('Data/Jack_Ma2.jpg')
img_jack_test = cv2.resize(img_jack_test, (800,500))

face_loc_jack = face_recognition.face_locations(img_jack)[0]
encode_jack = face_recognition.face_encodings(img_jack)[0]

face_loc_jack_test = face_recognition.face_locations(img_jack_test)[0]
encode_jack_test = face_recognition.face_encodings(img_jack_test)[0]

cv2.rectangle(img_jack,
              (face_loc_jack[1], face_loc_jack[2]),
              (face_loc_jack[3], face_loc_jack[0]),
              (255,0,255),
              2)
cv2.rectangle(img_jack_test,
              (face_loc_jack_test[1], face_loc_jack_test[2]),
              (face_loc_jack_test[3], face_loc_jack_test[0]),
              (255,0,255),
              2)

result = face_recognition.compare_faces([encode_jack], encode_jack_test)
distance = face_recognition.face_distance([encode_jack], encode_jack_test)

print(result, distance)

cv2.putText(img_jack_test,
            f'{result} {round(distance[0], 2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1, (0,0,255), 2)
cv2.imshow('Jack_Face', img_jack)
cv2.imshow('Jack_Face2', img_jack_test)
cv2.waitKey(0)
