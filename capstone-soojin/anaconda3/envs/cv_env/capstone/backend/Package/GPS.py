# gps 추출 코드
# 참고 사이트 : https://www.jbmpa.com/python_advanced/3
# 참고 영상 : https://www.youtube.com/watch?v=LocBtHjHUy0
# 참고 사이트 : http://bigdata.dongguk.ac.kr/lectures/DB/_book/python%EC%97%90%EC%84%9C-mysql%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A0%91%EA%B7%BC.html

# GPS 정보 추출
import numpy as np
from PIL.ExifTags import TAGS
# from PIL.Image import Image
import PIL.Image as Image
import pymysql
import pandas as pd
import cv2
from . import reverseGeocoding

# import sys
# print(sys.path)
# from os import path
# # 현재 위치
# print(path.abspath('.'))
# # 상위 폴더 위치
# print(path.abspath('..'))

def getexif(imgsrc) :
    # exif(날짜, 시간, GPS 추출)
    # 설명
    # imgsrc   => exif 추출할 이미지의 주소

    # 이미지 읽어들이기(한글 파일일 때도 가능 하게 -> numpy 사용하면 exif 안됨
    img = Image.open(imgsrc)
    img_info = img._getexif()

    # print("img : ", img)
    # print("img_info : ", img_info)

    global photo_time
    global photo_place
    global time
    global gps_1
    global gps_2



    # global res  
    # res = ''



    # GPSInfo 가 존재하는지 체크하기 위한 수단
    global GPSInfo_check 

    # 변수 리셋
    photo_time = ''
    time = ''
    GPSInfo_check = True

    # print('img_info : ', img_info)
    if img_info is None :
        # print('img_info is None')
        pass
    else :

        for tag_id in img_info :
            # print('tag_id : ', tag_id)
            # tag => exif 숫자를 단어로 바꿈(ex. 09112 -> GPS)
            tag = TAGS.get(tag_id, tag_id)

            if tag == 'DateTime' :
                data = img_info.get(tag_id)

                # DB : photo_time   / image table
                photo_time = (data.split(' ', 1)[0]).replace(':', '-')

                # DB : time         / image table
                time = data.split(' ', 1)[1]

                # print('tag : ', tag)
                # print('photo_time : ', photo_time)
                # print('time : ', time)
            if tag == 'GPSInfo' :
                data = img_info.get(tag_id)

                # GPSInfo -> 위도&경도
                gps = []

                # GPS 정보가 합쳐짐(ex. 34.0, 44.0, 25.0, 128.0, 11.0, 10.8)
                GPSInfo_tuple = data[2] + data[4]

                # GPSInfo 정보를 TT에 처리를 위해서 담기
                for GPSInfoData in GPSInfo_tuple :
                    gps.append(GPSInfoData)
                
                # GPSInfo -> 위도&경도
                gps = changeGPS(gps)

                # 위도&경도 -> gps_1 & gps_2
                gps = reverseGeocoding.get_address(gps[0], gps[1])
                gps_1 = gps.pop('gps_1')
                gps_2 = gps.pop('gps_2')
                photo_place = gps_2

                GPSInfo_check = False
            
    # exif에 GPSInfo 가 아예 없을 경우
    while(GPSInfo_check) :
        gps_1 = ''
        gps_2 = ''
        photo_place = ''
        break

 
    # DB에 삽입할 데이터 딕셔너리 형태로 저장
    # global finishDataDB
    finishDataDB = {'photo_time' : photo_time, 'photo_place' : photo_place, 'time' : time, 'gps_1' : gps_1, 'gps_2' : gps_2}

    return finishDataDB   


# GPS(exif) -> 위도&경도화
def changeGPS(TT) :
    # exif GPS를 위도&경도화 한 후 저장할 공간
    changeTT = []

    # TT : exifGPS -> 위도 & 경도 : 주소 변환 가능 상태로 변환
    # TT : notion[9.25회의 -> 용수진 > 09-27(메타 데이터에서 추출한..)] 참고

    # 위도 계산
    # 1. 3번째 값 / 60
    firstTT1 = 0
    firstTT2 = 0

    firstTT1 = TT[2]
    firstTT2 = firstTT1 / 60.
    TT[2] = firstTT2

    # 2. (2번째 + 3번째) / 60
    secondTT1 = 0
    secondTT2 = 0

    secondTT1 = TT[1] + firstTT2
    secondTT2 = secondTT1 / 60.
    TT[1] = secondTT2

    # 3. 1번째 + 2번째
    thridTT1 = 0

    thridTT1 = TT[0] + secondTT2
    changeTT.append(thridTT1)



    # 경도 계산
    # 1. 6번째 값 / 60
    firstTT1 = 0
    firstTT2 = 0

    firstTT1 = TT[5]
    firstTT2 = firstTT1 / 60.
    TT[5] = firstTT2

    # 2. (5번째 + 6번째) / 60
    secondTT1 = 0
    secondTT2 = 0

    secondTT1 = TT[4] + firstTT2
    secondTT2 = secondTT1 / 60.
    TT[4] = secondTT2

    # 3. 4번째 + 5번째
    thridTT1 = 0

    thridTT1 = TT[3] + secondTT2
    changeTT.append(thridTT1)

    # print('changeTT : ', changeTT)
    return changeTT

# print("Hello World")

# test
# print(getexif("C:/Users/rlawn/opencv/cv_env/capstone/image/testimg.jpg"))
# print(getexif("C:/Users/rlawn/opencv/cv_env/capstone/image/_exShareFolder/4.jpg"))
