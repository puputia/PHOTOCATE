import numpy as np
import os
import cv2
from . import mkdir
from . import DB_select as select

# 썸네일 생성 및 저장
def Thumbnail(img, folderName) :
    # 설명
    # img               => 이미지 저장 경로
    # folderName        => 공유폴더 이름
    # image             => 처리할 이미지(open)
    # imgName           => 이미지의 이름
    # imgExtension      => 이미지의 확장자
    # resized_image     => 썸네일 이미지

    # 이미지 읽어들이기(한글이어도 읽어들일 수 있게 수정)
    image_array = np.fromfile(img, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # 이미지 이름(imgNameAndExtension > 이름&확장자 | imgNameList > [이름, 확장자] | imgExtension > 확장자 | imgName > Thunbnail_&이름)
    imgNameAndExtension = img.rsplit('/', 1)
    imgNameList = imgNameAndExtension[1].rsplit('.', 1)
    imgExtension = imgNameList[1]
    imgName = "Thumbnail_" + imgNameList[0]

    # 매개변수에 넘어온 folderName이 실제로 존재하는 공유폴더인지 확인
    check_folderName = select.select('trip', 'tname', f"tname='{folderName}'")
    if len(check_folderName) == 1 :
        # photocate > 공유폴더 > 썸네일 폴더 없으면 폴더 생성!
        folderURL = 'C:/Users/Photocate' + "/" + folderName + '/' + '_ThumbnailFolder'
        mkdir.creatFolder(folderURL)

        # 저장될 썸네일 주소
        imgSrc =  folderURL + '/'+ imgName + '.' + imgExtension

        # print('imgSrc : ', imgSrc)

        # 썸네일 생성
        resized_image = cv2.resize(image, (180, 160))

        # 썸네일 저장(경로에 한글이 있을 경우에도 저장 하게 제작
        # 참고 사이트(https://blog-st.tistory.com/entry/Python-OpenCV-%ED%95%9C%EA%B8%80%EC%9C%A0%EB%8B%88%ED%8A%B8%EC%BD%94%EB%93%9C-%EA%B2%BD%EB%A1%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%97%B4%EA%B8%B0%EC%A0%80%EC%9E%A5)
        type = os.path.splitext(img)[1]
        ret, img_arr = cv2.imencode(type, resized_image)
        if ret :
           with open(imgSrc, mode='w+b') as f:
              img_arr.tofile(f)
        # cv2.imwrite(imgSrc, resized_image)
        # print("썸네일 저장 완료")

        return imgSrc
    
    elif len(check_folderName) == 0 :
        print("존재하지 않는 공유 폴더입니다. 다시 한 번 확인해주세요.")
    elif len(check_folderName) > 1 :
        print("같은이름의 공유 폴더가 다수 존재합니다. 다시 한 번 확인해주세요.")
    return 0



# 이미지가 업로드 되면 DB에 업데이트 될 예정 -> 그럴 때 자동으로 썸네일을 제작하여 저장하기!
# 이때, 썸네일 폴더가 있으면 그냥 저장만 하고 폴더 없으면 새로 생성하기
# _Thumbnail 폴더 생성(ThumbnailFolder.py 파일 불러오기)
# DB 와도 연결하기!(외부 파일과 연결하기 -> 물론, 외부 파일도 새로 제작^^)

# Test -> 성공
# imgURL = 'C:/Users/rlawn/opencv/cv_env/capstone/image/_exShareFolder/1.jpg'
# Thumbnail(imgURL, '친구들이랑')