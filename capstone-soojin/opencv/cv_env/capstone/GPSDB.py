# gps 추출 코드
# 참고 사이트 : https://www.jbmpa.com/python_advanced/3
# 참고 영상 : https://www.youtube.com/watch?v=LocBtHjHUy0
# 참고 사이트 : http://bigdata.dongguk.ac.kr/lectures/DB/_book/python%EC%97%90%EC%84%9C-mysql%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A0%91%EA%B7%BC.html

# GPS 정보 추출
import os
import pymysql
import numpy as np
import pandas as pd
from PIL import Image
import piexif
from glob import glob
from PIL.ExifTags import TAGS

# 튜플 형태를 문자열 형태로 변환
def tupleisstring(tup) :
    string = ''
    for a in tup :
        a = round(a)
        string += str(a) + " "
    return string

# DB 연결
def connectiondb():
    try:
        con = pymysql.connect(host="localhost", user="root", password="111111", port=3305, db="capstone", charset="utf8")
        return con
    except Exception as e:
        return e

# DB insert
def insertsql(giname, gdate, ghour, gresultgps) :
    try :
        with connectiondb() as con :
            with con.cursor() as cur :
                sql = f"UPDATE IMAGE SET DATE = '{gdate}', GPS = '{gresultgps}', TIME = '{ghour}' WHERE INAME = '{giname}';"
                # sql = str(sql)
                # print('sql : ', sql)
                cur.execute(sql)
                con.commit()
    except Exception as e :
        print("update 실패")
        print(e)
    
    # selectsql("image")
                
# DB select
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

# date & hour & GPS 데이터 출력 함수
def datehourgps(img) :
    # img = img.replace('\\', '/')
    giname = (((img.rsplit('\\', 1))[1]).rsplit('.', 1))[0]
    gdate = ''
    ghour = ''
    gresultgps = ''

    img = Image.open(f'{img}')

    # print('img : ', img)

    img_info = img._getexif()
    # print('getexif : ', img_info)
    for tag_id in img_info :
        # print('tag_id : ', tag_id)
        if (TAGS.get(tag_id, tag_id) == 'DateTime') or (TAGS.get(tag_id, tag_id) == 'GPSInfo') :
            # print("입성!")
            tag = TAGS.get(tag_id, tag_id)
            data = img_info.get(tag_id)
            # print("tag : ", tag)

            if tag == 'DateTime' :
                # print(f'촬영일시 : {data}')

                dsplit = data.split(' ')
                gdate = dsplit[0]
                ghour = (dsplit[1].split(':'))[0]

                # print('촬영날짜 : ', gdate)
                # # print('촬영시간 : ', ghour)
            
            if tag == 'GPSInfo' :
                # print(f'GPS : {data}')
                SN = str(data[1])
                EW = str(data[3])
                gps1 = tupleisstring(data[2])
                gps2 = tupleisstring(data[4])
                gresultgps = gps1 + SN + " " + gps2 + EW
                # print("gresultgps : ", gresultgps)

            insertsql(giname, gdate, ghour, gresultgps)
    return (giname, gdate, ghour, gresultgps)




# # 변환할 이미지 목록 불러오기
image_path = 'C:/Users/rlawn/Desktop/HYWU/23-1/capstone/testimg'
# testimg = Image.open("C:/Users/rlawn/opencv/cv_env/capstone/image/testimg.jpg")

# files = glob.glob(f"{image_path}./**/*.jpg")
file = []
files = glob(f"{image_path}/**/*.jpg") + glob(f"{image_path}/**/*.png") + glob(f"{image_path}/*.jpg") + glob(f"{image_path}/*.png")
# print(files)



# (이미지이름, GPS, 촬영날짜, 촬영일시) => 저장
# metadatasql = []

for a in files :

    # 촬영일시 -> date : 촬영일(년:월:일), hour : 촬영시간(시간)
    iname = ''
    gps = ''
    date = ''
    hour = ''

    # print('a : ', a)


    # print('iname, date, hour, gps : ',iname,  date, hour, gps)

    test = datehourgps(a)
    # print('test : ', test)
    # metadatasql.append(test)

selectsql("image")
# print(metadatasql)



















