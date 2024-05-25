# 특정 테이블을 삭제

import pymysql

def delete(tableName, searchCondition) :
    # 설명
    # tableName         => 삭제하고자 하는 DB 테이블
    # searchCondition   => 삭제하고자 하는 데이터의 조건(where)
    # sqlSentence       => sql delete 문 
    
    # DB 연결
    con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)
    cur = con.cursor()

    # sqlSentence
    sqlSentence = 'DELETE FROM ' + tableName + ' WHERE ' + searchCondition + ';'

    # print('sqlSentence : ', sqlSentence)
        
    # sql 실행
    cur.execute(sqlSentence)

    # sql 저장
    con.commit()

    # db 연결 종료(return으로 값을 보내기 전에 해도 되는지 의문???????)
    con.close()

    print("데이터 삭제 완료")


# print("Hello World : I', DB_delete")