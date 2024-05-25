# 참고 사이트 : https://data-make.tistory.com/170
# 입력창 생성 참고 사이트 : https://yeachan.tistory.com/6
import os
import pymysql
import pandas as pd

def creatFolder(directory):
    try : 
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.' + directory)

trip_url = 'C:/Users/rlawn/Desktop/HYWU/23-1/capstone/기말고사/공유폴더A'
tname = (trip_url.rsplit('/', 1))[1]
creatFolder(trip_url)

# 사용자에게 입력받은 ID/이름/전화번호 정보
userinput = input("ID/이름/전화번호 : ")
userinput = userinput.split("/")

startday = input("여행 시작 날짜(YYYY:MM:DD) : ")
finishday = input("여행 끝난 날짜(YYYY:MM:DD) : ")

user_id = userinput[0]
owner = user_id
name = userinput[1]
tel = userinput[2]




sql1 = "INSERT INTO user (USER_ID, NAME, TEL) VALUES(%s, %s, %s)"
sql2 = "INSERT INTO TRIP (TRIP_URL, OWNER, TNAME, STARTDAY, FINISHDAY) VALUES(%s, %s, %s, %s, %s)"

# 위에서 생성한 파일(공유폴더) 주소와 사용자 정보를 DB에 저장
# MySQL과 Connection 연결
con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)


with con:
    with con.cursor() as cur:
        cur.execute(sql1, (user_id, name, tel))
        con.commit()
        rows = cur.fetchall()
        # print(rows)

        # 데이터프레임 형태로 전환
        customers = pd.DataFrame(rows)
        # customers = pd.DataFrame(cur.fetchall())
        print(customers)



# 위에서 생성한 파일(공유폴더) 주소와 사용자 정보를 DB에 저장
# MySQL과 Connection 연결
con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)

try :
    with con:
        with con.cursor() as cur:
            cur.execute(sql2, (trip_url, owner, tname, startday, finishday))
            con.commit()
            rows = cur.fetchall()

            # 데이터프레임 형태로 전환
            customers = pd.DataFrame(rows)
            # customers = pd.DataFrame(cur.fetchall())
            print(customers)
except Exception as e :
    print("trip table insert 실패")
    print(e)