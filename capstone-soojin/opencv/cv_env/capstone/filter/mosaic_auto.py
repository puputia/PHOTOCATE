#참고 사이트 : https://blog.naver.com/PostView.naver?blogId=nkj2001&logNo=222747037611&parentCategoryNo=&categoryNo=95&viewDate=&isShowPopularPosts=false&from=postView

import numpy as np
import cv2
from matplotlib import pyplot as plt

# image = cv2.imread('image/faceTest.jpg') #이미지 읽어들이기
# image = cv2.imread('image/profTest1.jpg') #이미지 읽어들이기
image = cv2.imread('C:/Users/rlawn/opencv/cv_env/capstone/image/profTest2.jpg') #이미지 읽어들이기

# image = cv2.imread('image/profTest2.jpg') #이미지 읽어들이기
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #흑백 세팅
# 얼굴 인식을 위한 xml 파일 경로 설정(xml1 => 정면, xml2 => 측면)
# xml1 = 'C:/Users/rlawn/opencv/cv_env/capstone/Lib/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'
# xml2 = 'C:/Users/rlawn/opencv/cv_env/capstone/Lib/opencv-master/data/haarcascades/haarcascade_profileface.xml'

face_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #정면얼굴인식 파일 세팅
prof_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml') #측면얼굴인식 파일 세팅

faces = face_casecade.detectMultiScale(gray, 1.2, 5) #파일 설정
print("Number of faces detected: " + str(len(faces))) #인식된 얼굴 개수

prof = prof_casecade.detectMultiScale(gray, 1.2, 5) #파일 설정
print("Number of prof detected: " + str(len(prof))) #인식된 얼굴 개수

v = 20
if len(faces) :
    for (x, y, w, h) in faces :
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = image[y : y + h, x : x + w]

        # interpolation 부분이 함수처리를 이용해서 모자이크 필터를 적용하는 부분임
        # 이제 사용자가 모자이크 또는 블러, 색변환을 클릭한 내용을 받아서 적용하기
        #  예) 사용자가 모자이크를 선택했으면 0이라는 값이 프로그램에 들어와서 모자이크를 적용할 수 있도록 한다.
        roi = cv2.resize(roi_color, (w // v, h // v))
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
        image[y : y + h, x : x + w] = roi

if len(prof) :
    for (x, y, w, h) in prof :
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = image[y : y + h, x : x + w]

        roi = cv2.resize(roi_color, (w //v, h // v))
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
        image[y : y + h, x : x + w] = roi

# 처리한 이미지 저장하기
cv2.imwrite('C:/Users/rlawn/opencv/cv_env/capstone/image/after/mosaic_auto.jpg', image)

# 인식된 얼굴 화면에 그리기
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray') #이미지 보여주기
plt.xticks([]), plt.yticks([]) #x, y 설정
plt.show() #보여주기

