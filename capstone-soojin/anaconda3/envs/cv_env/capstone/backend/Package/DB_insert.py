# 특정 테이블에 데이터 삽입

import pymysql

def insert(tableName, tableSentence, valueSentence) :
    # 설명
    # tableName     => 삽입하고자 하는 테이블 명
    # tableSentence => 데이터 삽입 순서(ex. ('user_id', 'user_name', 'name'))
    # valueSentence => 스키마에 맞는 문장(ex. ('sj', 'soojin', '용수진'))
    # sqlSentence   => 최종 sql 문장

    # DB 연결
    con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)
    cur = con.cursor()

    # print('DB 연결 성공')

    # sqlSentence
    sqlSentence = 'INSERT INTO ' + tableName + ' ' + tableSentence + ' VALUES ' + valueSentence + ';'
    
    # print('sqlSentence : ', sqlSentence)
    
    # sql 실행
    cur.execute(sqlSentence)

    # sql 저장
    con.commit()

    # db 연결 종료(return으로 값을 보내기 전에 해도 되는지 의문???????)
    con.close()

    # print("데이터 삽입 완료")

# insert 테스트
# insert('user', '(user_id, name, tel)', "('soojinjin11111', '요요수진', '011-123-123')")

