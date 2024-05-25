#참고 사이트 : https://blog.naver.com/PostView.naver?blogId=nkj2001&logNo=222747037611&parentCategoryNo=&categoryNo=95&viewDate=&isShowPopularPosts=false&from=postView

import numpy as np
import cv2
from matplotlib import pyplot as plt
import pymysql
import pandas as pd

# DB 연결
def connectiondb():
    try:
        con = pymysql.connect(host="localhost", user="root", password="111111", port=3305, db="capstone", charset="utf8")
        return con
    except Exception as e:
        return e

# 사용자가 선택한 이미지의 이름을 이용해서 image table에서 image_url 정보 가져오기
def image_url(img) :
    try :
        with connectiondb() as con :
            with con.cursor() as cur :
                sql = f"SELECT IMAGE_URL FROM IMAGE WHERE INAME = '{img}'"
                cur.execute(sql)
                rows = cur.fetchall()
                # print('rpws : ',rows)
                rows = rows[0][0]
                return rows
    except Exception as e :
        print("image_url select 실패")
        print(e)

# 사용자의 이름을 토대로 user table에서 user_id 정보 가져오기
def user_id(una) :
    try :
        with connectiondb() as con :
            with con.cursor() as cur :
                sql = f"SELECT USER_ID FROM USER WHERE NAME = '{una}';"
                cur.execute(sql)
                rows = cur.fetchall()
                rows = rows[0][0]
                return rows
    except Exception as e :
        print("user_id select 실패")
        print(e)

# 필터 처리한 이미지 DB에 저장
def insertsql(after_imgurl, original_imgurl, userid) :
    try :
        with connectiondb() as con :
            with con.cursor() as cur :
                # original_imgurl = ('C:/Users/rlawn/Desktop/HYWU/23-1/capstone/testimg.\\22-12-07\\KakaoTalk_20230522_202510715.jpg')
                original_imgurl = original_imgurl.replace('\\', '\\\\')
                sql = f"INSERT INTO AFTERIMAGE (AFTER_URL, ORIGINAL_URL, USER_ID) VALUES('{after_imgurl}', '{original_imgurl}', '{userid}');"
                cur.execute(sql)
                con.commit()
    except Exception as e :
        print("afterimage insert 실패")
        print(e)

# select
def selectsql(table) :
    try :
        with connectiondb() as con :
            with con.cursor() as cur :
                sql = f"SELECT * FROM {table};"
                cur.execute(sql)
                rows = cur.fetchall()

                curstomers = pd.DataFrame(rows)
                print(curstomers)
    except Exception as e :
        print("select 실패")
        print(e)

def blurgo(src):
    return cv2.blur(src, (50, 50))

def blur_area(src, x, y, width, height):
    dst = src.copy()
    dst[y:y + height, x:x + width] = blurgo(dst[y:y + height, x:x + width])
    return dst

# 사용자가 편집을 하고자 선택한 이미지의 이름
aa = "KakaoTalk_20230522_202510715"
# 사용자 이름
uname = "수진"

image_url = image_url(aa)
user_id = user_id(uname)

# DB에서 가져온 내용 확인
# print('image_url : ', image_url)
# print('user_id : ', user_id)

# 필터 확인 이미지
# image = cv2.imread('C:/Users/rlawn/opencv/cv_env/capstone/image/faceTest.jpg', cv2.IMREAD_COLOR)

# 사용자가 선택한 이미지
image = cv2.imread(image_url) #이미지 읽어들이기


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #흑백 세팅

face_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #정면얼굴인식 파일 세팅
prof_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml') #측면얼굴인식 파일 세팅

faces = face_casecade.detectMultiScale(gray, 1.2, 5) #파일 설정
print("Number of faces detected: " + str(len(faces))) #인식된 얼굴 개수

prof = prof_casecade.detectMultiScale(gray, 1.2, 5) #파일 설정
print("Number of prof detected: " + str(len(prof))) #인식된 얼굴 개수

v = 20
if len(faces) :
    for (x, y, w, h) in faces :
        image = blur_area(image, x, y, w, h)


if len(prof) :
    for (x, y, w, h) in prof :
        image = blur_area(image, x, y, w, h)


# 처리한 이미지 저장하기
after_url = 'C:/Users/rlawn/opencv/cv_env/capstone/image/after/blur_auto.jpg'
cv2.imwrite(after_url, image)


# DB에 저장
insertsql(after_url, image_url, user_id)

# DB 확인
selectsql('afterimage')



# 처리된 이미지 사이즈 조절
small_iamge = cv2.resize(image, dsize=(800, 700))

# 인식된 얼굴 화면에 그리기
cv2.imshow("blur_auto", image)
cv2.waitKey(0)


