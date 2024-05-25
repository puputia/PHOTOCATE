# (함수화된) 필터 모은 파일!

import numpy as np
import cv2
from matplotlib import pyplot as plt
import pymysql
import pandas as pd
import os
from PIL import Image
import sys
from Package import *
import requests
import sys

# 한글 깨짐 해결
sys.stdout.reconfigure(encoding='utf-8')

# 여러 개의 파이썬 파일 실행(서버와 통신)
# url = 'http://localhost:5000/api/callPythonScripts/manyPythonFile'
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     # data['result'] = Python scripts executed successfully
#     print(data['result'])
#     # Test : 터미널에 해당 값이 입력 됨
#     print("이건 filter.py 입니다.")
# else:
#     print(f"Failed to call Python scripts. Status code: {response.status_code}")




# 1. blur_auto.py

# 사진의 영역을 파악해서 블러처리 : 얼굴 인식 한 후 호출되어 사용
def blur_area(src, x, y, width, height):
    dst = src.copy()
    dst[y:y + height, x:x + width] = cv2.blur(dst[y:y + height, x:x + width], (50,50))
    return dst
def blur_auto(img, folder) :
    # 설명
    # img       => 이미지 주소
    # folder    => '공유폴더/사용자폴더'
    # sj        => 사용자 아이디

    userID = folder.rsplit('/', 1)[1]

    # print("자동 블러 대상 파일 : ", img)

    #이미지 읽어들이기
    image = cv2.imdecode(np.fromfile(img, dtype=np.uint8), cv2.IMREAD_COLOR)

    #흑백 세팅
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #정면 & 측면얼굴인식 파일 세팅
    face_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
    prof_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml') 
    
    #파일 설정 & 정면 인식 개수
    faces = face_casecade.detectMultiScale(gray, 1.2, 5) 
    print("Number of faces detected: " + str(len(faces))) 

    #파일 설정 & 측면 인식 개수
    prof = prof_casecade.detectMultiScale(gray, 1.2, 5)
    print("Number of prof detected: " + str(len(prof)))

    
    # 얼굴 인식을 바탕으로 블러 처리
    # v = 20
    if len(faces) :
        for (x, y, w, h) in faces :
            image = blur_area(image, x, y, w, h)


    if len(prof) :
        for (x, y, w, h) in prof :
            image = blur_area(image, x, y, w, h)

    # 이미지 크기 정규화
    resized_image = cv2.resize(image, (600,600))


    # 자동 블러 처리한 이미지 보여주기(waitKey를 안해주면 그냥 pass하고 지나감)
    cv2.imshow("blurAuto", resized_image)
    cv2.waitKey(0)

    # 자동 블러 처리 후의 이미지 저장 경로(이미지는 기존 이름에 '_blurAuto'(사용한 필터) 를 붙이는 걸로!)
    saveImage('_blurAuto', img, folder, image, userID)


# 2. blur_not_auto.py
def blur_not_auto(imgURL, folder) :
    # 설명
    # imgURL    => 이미지의 실제 저장 경로명
    # folder    => '공유폴더/사용자폴더'    
    # # sj        => 사용자 아이디

    userID = folder.rsplit('/', 1)[1]

    # 이미지 경로를 통해 읽어들이기
    # img = cv2.imread(imgURL, cv2.IMREAD_COLOR)
    img = cv2.imdecode(np.fromfile(imgURL, dtype=np.uint8), cv2.IMREAD_COLOR)

    # 원본 이미지의 크기 확인
    height = img.shape[0]
    width = img.shape[1]
    print("원본 이미지의 크기 : ", width, " & ", height)

    # 이미지 크기 정규화
    resized_image = cv2.resize(img, (600,600))

    # windowName = 윈도우 창 이름을 지정하는 부분
    # 사용자가 특정 영역을 지정하면 거기에 해당하는 x, y, w, h 값을 리턴 받음
    # x, y는 사각형 좌상단 좌표(x,y)
    # w, h는 사각형의 width와 height를 의미
    # showCrossshair = False : 이미지의 영역을 지정할 때 십자가를 표시할지 말지 결정하는 인자
    x, y, w, h = cv2.selectROI(windowName='blur -> not auto', img=resized_image, showCrosshair=False)

    # 선택한 구역의 이미지 픽셀값을 image_loc에 저장하고 blur 처리
    # 커널 사이즈는 (50, 50)으로 처리
    image_loc = resized_image[y : y + h, x : x + w]
    image_loc = cv2.blur(image_loc, (50, 50))

    # blur 처리한 이미지를 원본의 동일 위치에 덧붙임
    image_w_blur = resized_image
    image_w_blur[y : y + h, x : x + w] = image_loc

    # selecROI 함수에 의해 출력된 그림파일을 없앰
    cv2.destroyAllWindows()

    image = image_w_blur

    # blur로 흐림처리된 이미지를 불러옴
    cv2.imshow("Blur", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 이미지 크기 원상복구
    image = cv2.resize(image, (width,height))

    # 자동 블러 처리 후의 이미지 저장 경로(이미지는 기존 이름에 '_blurAuto'(사용한 필터) 를 붙이는 걸로!)
    saveImage('_blurNotAuto', imgURL, folder, image, userID)


# 3. mosaic_auto
def mosaic_auto(img, folder) :
    # 설명
    # img       => 이미지 주소
    # folder    => '공유폴더/사용자폴더'    
    # # sj        => 사용자 아이디

    userID = folder.rsplit('/', 1)[1]

    # 이미지 읽어들이기
    # image = cv2.imread(img)
    image = cv2.imdecode(np.fromfile(img, dtype=np.uint8), cv2.IMREAD_COLOR)

    # 흑백세팅
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #정면 & 측면얼굴인식 파일 세팅
    face_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
    prof_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml') 
    
    #파일 설정 & 정면 인식 개수
    faces = face_casecade.detectMultiScale(gray, 1.2, 5) 
    print("Number of faces detected: " + str(len(faces))) 

    #파일 설정 & 측면 인식 개수
    prof = prof_casecade.detectMultiScale(gray, 1.2, 5)
    print("Number of prof detected: " + str(len(prof)))

    
    # 얼굴 인식을 바탕으로 모자이크 처리
    v = 20
    if len(faces) :
        for (x, y, w, h) in faces :
            # roi_gray = gray[y : y + h, x : x + w]
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
            # roi_gray = gray[y : y + h, x : x + w]
            roi_color = image[y : y + h, x : x + w]

            roi = cv2.resize(roi_color, (w //v, h // v))
            roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
            image[y : y + h, x : x + w] = roi

    # 이미지 크기 정규화
    resized_image = cv2.resize(image, (600,600))


    # 자동 블러 처리한 이미지 보여주기(waitKey를 안해주면 그냥 pass하고 지나감)
    cv2.imshow("mosaicAuto", resized_image)
    cv2.waitKey(0)

    # 자동 블러 처리 후의 이미지 저장 경로(이미지는 기존 이름에 '_blurAuto'(사용한 필터) 를 붙이는 걸로!)
    saveImage('_mosaicAuto', img, folder, image, userID)
    

# 4. mosaic_not_auto
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst
def mosaic_not_auto(imgURL, folder) :
    # 설명
    # imgURL    => 이미지의 실제 저장 경로명
    # folder    => '공유폴더/사용자 폴더'
    # sj        => 사용자 아이디

    userID = folder.rsplit('/', 1)[1]

    # 이미지 경로를 통해 읽어들이기
    # img = cv2.imread(imgURL, cv2.IMREAD_COLOR)
    img = cv2.imdecode(np.fromfile(imgURL, dtype=np.uint8), cv2.IMREAD_COLOR)

    # 원본 이미지의 크기 확인
    height = img.shape[0]
    width = img.shape[1]
    print("원본 이미지의 크기 : ", width, " & ", height)

    # 이미지 크기 정규화
    resized_image = cv2.resize(img, (600,600))

    # windowName = 윈도우 창 이름을 지정하는 부분
    # 사용자가 특정 영역을 지정하면 거기에 해당하는 x, y, w, h 값을 리턴 받음
    # x, y는 사각형 좌상단 좌표(x,y)
    # w, h는 사각형의 width와 height를 의미
    # showCrossshair = False : 이미지의 영역을 지정할 때 십자가를 표시할지 말지 결정하는 인자
    x, y, w, h = cv2.selectROI(windowName='mosaic -> not auto', img=resized_image, showCrosshair=False)

    # 모자이크 처리
    dst_area = mosaic_area(resized_image, x, y, w, h)

    # selecROI 함수에 의해 출력된 그림파일을 없앰
    cv2.destroyAllWindows()

    # 모자이크 된 이미지 출력
    cv2.imshow('mosaic not auto', dst_area)
    cv2.waitKey(0)

    dst_area = cv2.resize(dst_area, (width, height))

    # 자동 모자이크 처리 후의 이미지 저장 경로(이미지는 기존 이름에 '_mosaicNotAuto'(사용한 필터) 를 붙이는 걸로!)
    saveImage('_mosaicNotAuto', imgURL, folder, dst_area, userID)


# 5. black
def black(img, folder) :
    # 설명
    # img       => 이미지 주소
    # folder    => '공유폴더/사용자폴더'
    # userID        => 사용자 아이디

    userID = folder.rsplit('/', 1)[1]

    # 이미지 불러와서 image 변수에 입력
    # image = cv2.imread(img)
    image = cv2.imdecode(np.fromfile(img, dtype=np.uint8), cv2.IMREAD_COLOR)

    # 흑백세팅
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지 크기 정규화
    resized_image = cv2.resize(gray, (600,600))

    # 흑백으로 변환된 이미지 출력
    cv2.imshow('black', resized_image)
    cv2.waitKey(0)


    # 자동 모자이크 처리 후의 이미지 저장 경로(이미지는 기존 이름에 '_mosaicNotAuto'(사용한 필터) 를 붙이는 걸로!)
    saveImage('_black', img, folder, gray, userID)


# 필터 처리 후 이미지 저장a
def saveImage(filter, original_url, folder, after_img, useID) :
    # 설명
    # filter            => 방금 전에 처리된 필터명(예> blurNotAuto)
    # original_url      => 원본 이미지 경로명
    # folder            => '공유폴더/사용자 폴더' 경로명
    # after_img         => 필터 처리 된 이미지
    # userID            => 사용자 아이디

    # 필터 처리 된 적 있는 이미지 여부
    global check
    check = 0

    imgName = original_url.rsplit('/', 1)
    imgNameList = imgName[1].rsplit('.', 1)
    imageName = imgNameList[0] + filter + '.' + imgNameList[1]

    # 이미지 저장은 모든 이미지들이 있는 폴더 하위에 사용자 이름 혹은 id의 폴더 하위에 저장된다.
    after_url = folder + '/' + imageName

    # after 이미지 저장
    # cv2.imwrite(after_url, after_img)


    # # 필터 처리가 된 적 있는 이미지일 경우 (_blurAuto, _blurNotAuto, _mosaicAuto, _mosaicNotAuto, _black 등의 문구과 있을 것) -> 기존 이미지 삭제 하기
    # filterHistory = imgNameList[0].split('_')

    # checkHistory = ['blurAuto', 'blurNotAuto', 'mosaicAuto', 'mosaicNotAuto', 'black']
    # i = 1
    # while(len(filterHistory) >= (i+1)) :
    #     if filterHistory[i] in checkHistory :
    #         print("필터 처리 된 적 있는 이미지 입니다.")

    #         # filter 처리 된 이미지라는 표시!
    #         check = 1

    #         break
    #     else :
    #         print("비교 내용 : ", filterHistory[i])
    #         print("필터 처리 된 적 없는 이미지 입니다.")
    #         i+=1

    # 필터 처리가 된 적 있는 이미지일 경우 -> DB에 원본 이미지의 url이 이미 있다.
    checkHistory = DB_select.select('afterimage', 'original_url', f"original_url = '{original_url}' and user_id = '{useID}'")
    
    print('checkHistory : ', checkHistory)

    if len(checkHistory) == 1 :
        # 해당 이미지는 기존의 filter 처리 된 적이 있다.
        # 해야 할 일 (1. 과거의 처리된 이미지 삭제-after_url 2. DB 수정-after_url)
        deleteAfter_url = DB_select.select('afterimage', 'after_url', f"original_url = '{original_url}' and user_id = '{useID}'")[0]
        os.remove(deleteAfter_url)
        DB_update.update('afterimage', f"after_url = '{after_url}'", f"original_url = '{original_url}' and user_id = '{useID}'")

    elif len(checkHistory) > 1 :
        # 해당 이미지는 기존의 filter 처리가 된 적이 있다. & 과거의 기록이 비정상적으로 많은 상태(원래는 많아도 1개의 데이터여야 하는데 기존이 제대로 삭제가 안 된 상태)
        deleteAfter_url_list = DB_select.select('afterimage', 'after_url', f"original_url = '{original_url}' and user_id = '{useID}'")
        print('deleteAfter_url_list : ', deleteAfter_url_list)
        checkvalue = 0
        while len(deleteAfter_url_list) >= checkvalue+1 :
            print('deleteAfter_url_list[checkvalue] : ', deleteAfter_url_list[checkvalue])
            os.remove(deleteAfter_url_list[checkvalue])
            DB_delete.delete('afterimage', f"after_url = '{deleteAfter_url_list[checkvalue]}'")
            checkvalue += 1
        # DB insert
        DB_insert.insert('afterimage', '(after_url, original_url, user_id)', f"('{after_url}', '{original_url}', '{useID}')")
        print("insert 완료")
    elif len(checkHistory) == 0 :
        # DB insert
        DB_insert.insert('afterimage', '(after_url, original_url, user_id)', f"('{after_url}', '{original_url}', '{useID}')")
        print("insert 완료")
    
    # after 이미지 저장(한글 경로여도 저장 될 수 있도록!)
    type = os.path.splitext(original_url)[1]
    ret, img_arr = cv2.imencode(type, after_img)
    if ret :
        with open(after_url, mode='w+b') as f :
            img_arr.tofile(f)

    print("after 이미지 저장 경로(저장했어요! 확인해보세요!) : ", after_url)


    # # 기존의 필터 처리가 된 적 있는 이미지 일 경우 삭제 해주기!
    # if check == 1 :
    #     print("필터 처리가 된 적 있는 기존 이미지는 삭제하도록 할게요!")
    #     os.remove(original_url)
    #     print("삭제 완료!")
    
   

# filter 작동 메인 함수
def filter(filter, img_url, shareFolderName, userData) :
    # 설명
    # filter            => 이미지 편집에 사용할 filter 종류
    # img_url           => 필터 처리할 이미지의 저장 주소
    # shareFolderName   => 이미지가 속한 공유폴더 이름
    # userData          => 현재 처리하고자 하는 주체, 사용자의 id

    
    # 필터 처리한 이미지를 저장할, 사용자 폴더 생성(없으면 생성, 있으면 진행)
    userFolder = mkdir.filtermkdir(img_url, userData, shareFolderName)

    # print("filter-mkdir 실행 결과 : ", userFolder)

    if 'C:/Users/Photocate/' not in userFolder :
        return userFolder
    else :
        if filter == 'blur_auto' :
            blur_auto(img_url, userFolder)
        elif filter == 'blur_not_auto' :
            blur_not_auto(img_url, userFolder)
        elif filter == 'mosaic_auto' : 
            mosaic_auto(img_url, userFolder)
        elif filter == 'mosaic_not_auto' :
            mosaic_not_auto(img_url, userFolder)
        elif filter == 'black' :
            black(img_url, userFolder)
        else :
            return "종류를 다시 한번 확인해주세요."



filter('mosaic_not_auto', 'C:/Users/Photocate/친구들이랑/place-none/2022-08-23/3.jpg', '친구들이랑', 'sj')

# print("hello 바나나!")




