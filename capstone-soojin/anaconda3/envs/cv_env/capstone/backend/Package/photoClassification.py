# https://post.naver.com/viewer/postView.nhn?volumeNo=28851017&memberNo=34865381

# 사진 정보 확인
import glob


import os
import shutil
from PIL import Image
from PIL import ExifTags
import numpy as np
import cv2
from . import DB_insert as insert
from . import DB_select as select

def classification(imgURL, tripURL, place, time) :
    # 설명
    # imgURL        => 이미지가 실제로 저장된 주소
    # tripURL       => 공유폴더 주소 -> 이미지들을 이곳으로 이동시키기
    # place         => 위치(장소)별 분류    [photo_place == gps_2]
    # time          => 날짜별 분류          [photo_time]
    # folder2save   => 이미지를 이동할 위치(공유폴더/time)


    
    # 날짜별로 분류 진행
    folder2save = tripURL + '/' + place + '/' + time
    if not os.path.exists(folder2save) :
        os.makedirs(folder2save)

    # classification DB 확인 후 채우기
    # data가 이미 저장된 것인지 확인
    checkclassification = select.select('classification', 'trip_url', f"maingroup = '{place}' AND subgroup = '{time}'")
    # print('checkclassification : ', checkclassification)
    if len(checkclassification) == 0 :
        # classifiation DB 채우기
        insert.insert('classification', '(maingroup, subgroup, trip_url)', f"('{place}', '{time}', '{tripURL}')")
    elif len(checkclassification) == 1 :
        pass
    elif len(checkclassification) > 1 :
        return "[관리자에게 전달해주세요] classification가 중복됐습니다."
    # 이미지 옮기기
    shutil.move(imgURL, folder2save)

    return "이미지 분류&이동 종료"
    
        
        


