{
# 참고 사이트 : https://thinking-developer.tistory.com/62
# 현재 폴더 안에 다른 폴더가 있으면 그 안에 이미지는 안 긁어옴..
# 그리고 25번째 줄 오류 발생..!
}
{
# img_list = os.listdir(image_path) #디렉토리 내 모든 파일 불러오기
# img_list_jpg = [img for img in img_list if img.endswith(".jpg")] #지정된 확장자만 필터링

# print("img_list_jpg : {}" .format(img_list_jpg))


# img_list_np = []

# for i in img_list_jpg:
#     img = Image.open(image_path + i)
#     img_array = np.array(img)
#     img_list_np.append(img_array)
#     print(i, "추가 완료 - 구조 : ", img_array.shape) #불러운 이미지의 차원 확인(세로X가로X색)
#     # print(img_array.T.shape) #축변경(색X가로X세로)

#     # img_np = np.array(img_list_np) # 리스트를 numpy로 변환
#     # print(img_np.shape)
}

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

# 사진 용량 -> MB/KB 등 함수
# 참고 사이트 : https://zephyrus1111.tistory.com/171

def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
def connectiondb():
    try:
        con = pymysql.connect(host="localhost", user="root", password="111111", port=3305, db="capstone", charset="utf8")
        return con
    except Exception as e:
        return e

# # 변환할 이미지 목록 불러오기
image_path = 'C:/Users/rlawn/Desktop/HYWU/23-1/capstone/testimg'

# MySQL Connection 연결
con = pymysql.connect(host="localhost", user="root", password="111111", db="capstone", charset="utf8", port=3305)

# files = glob.glob(f"{image_path}./**/*.jpg")
files = glob(f"{image_path}./**/*.jpg") + glob(f"{image_path}./**/*.png") + glob(f"{image_path}./*.jpg") + glob(f"{image_path}./*.png")
i = 0

# DB에 insert할 데이터들이 들어갈 곳!
arraylist = []
testtest = []

for a in files :
    # print(i , " : ", a)

    # data
    image_url = a

    a_iname = (a.rsplit('\\', 1))[1]
    iname = (a_iname.rsplit('.', 1))[0]

    # 사진 용량(MB 등)
    size = os.path.getsize(a)
    image_size = convert_size(size)

    date = '?'
    thumb_url = '?'
    gps = '?'
    time = '?'

    al = (image_url, iname, image_size, date, thumb_url, gps, time)

    # print('iname : ', iname)
    # print('image_size : ', image_size)

    
    arraylist.append(al)


    i+=1

# print('arraylist : ', arraylist)

# DB에 저장
# connection으로 부터 cursor 생성
# cur = con.cursor()


# SQL문 insert => 1번만 실행하기
sql = "INSERT INTO IMAGE (image_url, iname, image_size, date, thumb_url, gps, time) values(%s, %s, %s, %s, %s, %s, %s);"

try:
    with connectiondb() as con:
        with con.cursor() as cur :
            cur.executemany(sql, arraylist)
            con.commit()
except Exception as e:
    print("insert 실패 : 이미 데이터 삽입 완료")
    print(e)






# con = pymysql.connect(host="localhost", user="root", password="111111", db="capstone", charset="utf8", port=3305)
try:
    with connectiondb() as con:
        with con.cursor() as cur :
            # SQL문 실행 및 fetch
            sql = "SELECT * FROM IMAGE"
            cur.execute(sql)
            rows = cur.fetchall()

            # 데이터프레임 형태로 전환
            customers = pd.DataFrame(rows)
            # customers = pd.DataFrame(cur.fetchall())
            print(customers)

except Exception as e:
    print("select 실패")
    print(e)
