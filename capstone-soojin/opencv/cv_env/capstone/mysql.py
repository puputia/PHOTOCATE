# 참고 사이트 : http://bigdata.dongguk.ac.kr/lectures/DB/_book/python%EC%97%90%EC%84%9C-mysql%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A0%91%EA%B7%BC.html

import pymysql

# MySQL과 Connection 연결
con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)

# connection으로 부터 cursor 생성
cur = con.cursor()

# # sql문 실행 및 fetch
# sql = "SELECT * FROM user;"
# cur.execute(sql)

# # 데이터 fetch
# rows = cur.fetchall()
# print(rows)

# # db 연결 종료
con.close()