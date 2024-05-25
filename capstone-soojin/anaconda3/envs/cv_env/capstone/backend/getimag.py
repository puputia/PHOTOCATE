{
    # 참고 사이트1 : https://badlec.tistory.com/283
    # 참고 사이트2 : https://resumetmachine.tistory.com/entry/%ED%8F%B4%EB%8D%94%EC%99%80-%ED%95%98%EC%9C%84%ED%8F%B4%EB%8D%94-%ED%8C%8C%EC%9D%BC-%EB%AA%A9%EB%A1%9D-%EB%A7%8C%EB%93%A4%EA%B8%B0-globglob
}
import os
import numpy as np
from PIL import Image
from glob import glob
import pymysql
import pandas as pd
import shutil
import Package.GPS as gpsdata
import Package.Thumbnail as Thumbnail
import Package.mkdir as mkdir
import Package.reverseGeocoding as geocoding
import Package.photoClassification as photoClassification
import Package.DB_select as select
import Package.DB_insert as insert
import requests
import sys

# 한글 깨짐 해결
sys.stdout.reconfigure(encoding='utf-8')

# 여러 개의 파이썬 파일 실행(서버와 통신)
url = 'http://localhost:5000/api/callPythonScripts/manyPythonFile'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['result'])
else:
    print(f"Failed to call Python scripts. Status code: {response.status_code}")



# 사진 용량 -> MB/KB 등 함수
# 참고 사이트 : https://zephyrus1111.tistory.com/171

# 이미지 사이즈 구하는 함수
def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def getimage(image_path, shareFolderName, nowUSER, startDay, finishDay, creation) :
    # 설명
    # image_path        => 업로드할 이미지들 폴더(개별 이미지x 폴더) ->> 폴더 하위에 이미지 전부 처리!
    # shareFolderName   => 공유폴더 이름
    # nowUSER           => 공유폴더를 만들려고 하는 사용자 id
    # startDay          => 여행 시작일
    # finsith           => 여행 종료일
    # creation          => 공유 폴더를 새로 생성하는 것인지 혹은 이미지만 추가로 업로드 하는 것인지 확인(새로 생성 => Y, 이미지 업로드 => N)


    if len(select.select('user', 'user_id', f"user_id='{nowUSER}'")) != 1 :
            return "아이디를 다시 한 번 확인해주세요."
    else :
        if creation == 'N' :
            if len(select.select('trip', 'tname', f"tname='{shareFolderName}'")) < 1 :
                return "업로드 하고자 하는 공유 폴더가 존재하지 않습니다. 다시 한 번 확인해주세요."
            elif len(select.select('trip', 'tname', f"tname='{shareFolderName}'")) == 1 :
                # 공유폴더 안 만들고 처리!
                pass
        elif creation == 'Y' :
            if len(select.select('trip', 'tname', f"tname='{shareFolderName}'")) > 0 :
                return "공유 폴더 이름이 중복됩니다. 다시 한 번 확인해주세요."
            elif len(select.select('trip', 'tname', f"tname='{shareFolderName}'")) == 0 :
                # 공유폴더 만들고 처리!
                mkdir.mkdir(shareFolderName, nowUSER, startDay, finishDay)



    # 이미지 정보 가져오기
    files = glob(f"{image_path}/**/*.jpg") + glob(f"{image_path}/**/*.png") + glob(f"{image_path}/*.jpg") + glob(f"{image_path}/*.png")

    # print(files)

    # 이미지들 DB에 삽입
    # 설명
    # changeImageAddress    => 슬래쉬가 통일된 젼체 경로(경로 + 파일명 + 확장자)
    # image_all_url     => 이미지의 전체 url를 리스트로 쪼갬
    # imgae_url         => 정리된 이미지의 전체 url
    # iname             => 이미지 이름
    # image_size        => 이미지 사이즈
    # image_type        => 이미지의 확장자(db에는 type이라는 이름으로 되어있음) => 유의하자아앙!
    # after_image_url   => 공유폴더 하위로 이동시킨 이미지의 주소

    i = 0
    while(len(files) > i) : 
        # 전체 경로 슬래쉬 통일
        changeImageAddress = files[i].replace('\\','/')
        # 통일된 전체 경로 리스트로 쪼개기(경로, 파일명+확장자)
        image_all_url = changeImageAddress.rsplit('/', 1)
        # 파일명과 확장자 리스트로 쪼개기(파일명, 확장자)
        image = image_all_url[1].rsplit('.', 1)
        # 공유폴더 경로
        react_tripURL = 'C:/Users/Photocate' + '/' + shareFolderName

        # iname & image_url
        iname = image[0]
        image_type = image[1]
        image_url = image_all_url[0] + '/' + iname + '.' + image_type


        # image_size
        size = os.path.getsize(files[i])
        image_size = convert_size(size)

        # thumb_url
        thumb_url = Thumbnail.Thumbnail(image_url, shareFolderName)
        
        # trip_url
        # 공유폴더의 url을 react에서 가져와서 진행 -> 공유폴더를 만들고 그 안에서 이미지를 업로드 할 것임. 그러면 react에서 해당 공유폴더 url 정보를 넘겨주면 됨. 암튼 그럼.
        trip_url = select.select('trip', 'trip_url', f"trip_url='{react_tripURL}'")[0]
        
        # date, time, gps
        # print('image_url : ', image_url)
        photo_time_time_gps_1_2 = gpsdata.getexif(image_url)
        # print('date_time_gps_dic : ', date_time_gps_dic)
        photo_time = photo_time_time_gps_1_2['photo_time'].strip()
        photo_place = photo_time_time_gps_1_2['photo_place'].strip()
        time = photo_time_time_gps_1_2['time']
        gps_1 = photo_time_time_gps_1_2['gps_1']
        gps_2 = photo_time_time_gps_1_2['gps_2']

        # 분류
        # time 정보가 없을 경우
        if photo_time == '' :
            photo_time = 'time-none'
        # place 정보가 없을 경우
        if photo_place == '' :
            photo_place = 'place-none'

        # photoClassification_place & time
        photoClassificationText = photoClassification.classification(image_url, trip_url, photo_place, photo_time)
        # print('photoClassificationText : ', photoClassificationText)


        # 이미지 공유폴더 하위로 이동시키기(복사x)
        # shutil.move(changeImageAddress, react_tripURL)
        # print(changeImageAddress)
        # print(react_tripURL)

        # 공유 폴더 하위로 이동시킨 이미지의 경로
        after_image_url = react_tripURL + '/' + iname + '.' + image_type
        # print("공유폴더 하위로 이동한 후 경로 : ", after_image_url)
        
        # DB select (trip_url)
        # trip_url = select('trip', 'trip_url', f"trip_url = '{trip_url}'")[0]

        
        # DB insert
        # 데이터 값 추가!(gps_1, gps_2, photo_place, photo_time)
        insert.insert('image', '(image_url, trip_url, iname, image_size, thumb_url, time, type, gps_1, gps_2, photo_time, photo_place)'
               , f"('{after_image_url}', '{trip_url}', '{iname}', '{image_size}', '{thumb_url}', '{time}', '{image_type}', '{gps_1}', '{gps_2}', '{photo_time}', '{photo_place}')")

        # check
        # print('image_url : ', after_image_url)
        # print('photo_time : ', photo_time)
        # print('photo_place : ', photo_place)
    
        # cf_image DB 채우기
        insert.insert('cf_image', '(original_url, maingroup, subgroup)', f"('{after_image_url}', '{photo_place}', '{photo_time}')")
        i+=1
    return "이미지 업로드가 끝났습니다."

# test
# print(getimage('C:/Users/rlawn/anaconda3/envs/cv_env/capstone/image', '친구들이랑', 'sj', '2023:11:10', '2023:12:10', 'Y'))

