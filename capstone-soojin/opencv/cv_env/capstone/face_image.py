#참고 사이트 : https://www.youtube.com/watch?v=Mso5v2hcoFs

import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('image/profTest2.jpg') #이미지 읽어들이기
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #흑백 세팅
# 얼굴 인식을 위한 xml 파일 경로 설정(xml1 => 정면, xml2 => 측면)
xml1 = 'Lib/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'
xml2 = 'Lib/opencv-master/data/haarcascades/haarcascade_profileface.xml'

face_casecade = cv2.CascadeClassifier(xml1) #정면얼굴인식 파일 세팅
prof_casecade = cv2.CascadeClassifier(xml2) #측면얼굴인식 파일 세팅

faces = face_casecade.detectMultiScale(gray, 1.2, 5) #파일 설정
print("Number of faces detected: " + str(len(faces))) #인식된 얼굴 개수

prof = prof_casecade.detectMultiScale(gray, 1.2, 5) #파일 설정
print("Number of prof detected: " + str(len(prof))) #인식된 얼굴 개수

if len(faces) :
    for (x, y, w, h) in faces :
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

if len(prof) :
    for (x, y, w, h) in prof :
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 인식된 얼굴 화면에 그리기
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray') #이미지 보여주기
plt.xticks([]), plt.yticks([]) #x, y 설정
plt.show() #보여주기