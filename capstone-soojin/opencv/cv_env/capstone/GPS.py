# gps 추출 코드
# 참고 사이트 : https://www.jbmpa.com/python_advanced/3
# 참고 영상 : https://www.youtube.com/watch?v=LocBtHjHUy0
# 참고 사이트 : http://bigdata.dongguk.ac.kr/lectures/DB/_book/python%EC%97%90%EC%84%9C-mysql%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A0%91%EA%B7%BC.html

# GPS 정보 추출
from PIL import Image
from PIL.ExifTags import TAGS
import pymysql
import pandas as pd

# 위 코드를 그냥 함수로 안만드는 방법으로 조금 수정함
img = Image.open("C:/Users/rlawn/opencv/cv_env/capstone/image/testimg.jpg")
# img = Image.open("C:/Users/rlawn/Desktop/HYWU/23-1/capstone/testimg/22-12-07/KakaoTalk_20230522_202510715_19.jpg")

img_info = img._getexif()


# 촬영일시 -> date : 촬영일(년:월:일), hour : 촬영시간(시간)
date = ''
hour = ''
gps = ''
res = ''

# (GPS, 촬영날짜, 촬영일시) => 저장
metadatasql = []

for tag_id in img_info :
    tag = TAGS.get(tag_id, tag_id)
    data = img_info.get(tag_id)
    # 현재 tag 안에는 ImageWidth & ImageLength & GPSInfo 데이터밖에 없어서 DateTime if문이 실행이 안됨

    if tag == 'DateTime':
        print(f'촬영일시 : {data}')

        # 촬영일시 년-월-일 시 로 절사
        dsplit = data.split(' ')
        date = dsplit[0]
        hour = (dsplit[1].split(':'))[0]

        print('촬영날짜 : ', date)
        print('촬영시간 : ', hour)
                
    # print('다 나와서 date : ', date)
    if tag == 'GPSInfo':
        info = img._getexif()

        # 새로운 딕셔너리 생성
        taglabel = {}
        
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            taglabel[decoded] = value
        
        exifGPS = taglabel['GPSInfo']

        # 위치 정보 저장할 공간
        for i in exifGPS:
            # index 1부터 시작
            # print(i)

            k = 1
            if (i%2 == 0) and (i != 6):
                # print("1. i :", i)
                # print("2. exifGPS : ", exifGPS)
                for j in exifGPS[i]:
                    # print("3. i : ", i)
                    # print("4. exifGPS : ", exifGPS)
                    # print('5. j : ' , j)
                    # print("6. iter(exifGP) : ", iter(exifGPS))
                    res += str(round(j)) + " " #round() -> 소수점 절삭, 이유 : 소수점이 있는 상태로는 구글 지도에서 검색이 안됨(정수만 가능)
                # 북위 or 남위
                if exifGPS[i-1] == 'S':
                    # ww = -1.0
                    # print('ww', ww)
                    res += 'S'
                elif exifGPS[i-1] == 'N':
                    res += 'N'
                # 동경 or 서경
                if exifGPS[i-1] == 'W':
                    # kk = -1.0
                    # print('kk', kk)
                    res += 'W'
                elif exifGPS[i-1] == 'E' :
                    res += 'E'
# GPS 정보를 출력
print('촬영장소 : ', res)
gps = res

metadatasql.append((res, date, hour))
print(metadatasql)












# MySQL에 데이터 저장

# MySQL Connection 연결
# con = pymysql.connect(host="localhost", user="root", password="111111", db="capstone", charset="utf8", port=3305)

# connection으로 부터 cursor 생성
# cur = con.cursor()

{
    # insert 성공!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 1번만 실행해줘야 함! 안그러면 pk 중복으로 오류 발생
    # 외래키 테이블을 먼저 입력해줘야 함. 만약 외래키 테이블 먼저 입력 안하고 그냥
    # test 하고 싶으면 그냥 데이터를 안 넣어주면 됨.

    # SQL문 insert
    # sql = "INSERT INTO IMAGE (image_url, iname, image_size, date, thumb_url, gps, time) values(%s, %s, %s, %s, %s, %s, %s);"

    # with con:
    #     with con.cursor() as cur :
    #         cur.execute(sql, ('hp://~', 'hey', 900, date, 'hp2://', res, hour))
    #         con.commit()
}

{
    # insert 성공!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 1번만 실행해줘야함! 안그러면 pk 중복으로 오류 발생
    # SQL문 insert -> USER
    # sql = "INSERT INTO USER (user_id, name, tel) values (%s, %s, %s);"

    # with con:
    #     with con.cursor() as cur:
    #         cur.execute(sql, ('asas', 'sj', '010-1111-1111'))
    #         con.commit()
}

# # connection으로 부터 cursor 생성
# # => with 끝나고는 cursor()가 닫힌다고 해서 아래 문을 그냥 하면 오류 발생
# cur = con.cursor()

# # SQL문 실행 및 fetch
# sql = "SELECT * FROM IMAGE;"
# cur.execute(sql)

# # 데이터 fetch
# rows = cur.fetchall()
# # print(rows)

# # db 연결 종료
# con.close()

# # 데이터프레임 형태로 전환
# customers = pd.DataFrame(rows)
# print(customers)