# 특정 테이블에 데이터 수정

import pymysql

def update(tableName, setColumnSentence, conditionSentence) :
    # 설명
    # tableName         => 삽입하고자 하는 테이블 명
    # setColumnSentence => 변경하고자 하는 컬럼명과 변경 데이터(ex. name='용수진')
    # conditionSentence => 변경하고자 하는 컬럼의 조건(where| ex. name='요요수진')
    # sqlSentence       => 최종 sql 문장

    # DB 연결
    con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)
    cur = con.cursor()

    # print('DB 연결 성공')

    # sqlSentence
    sqlSentence = 'UPDATE ' + tableName + ' SET ' + setColumnSentence + ' WHERE ' + conditionSentence + ';'
    
    # print('sqlSentence : ', sqlSentence)
    
    # sql 실행
    cur.execute(sqlSentence)

    # sql 저장
    con.commit()

    # sql 종료
    con.close()

    print("데이터 변경 완료")

# update 테스트
# update('user', "name='용수진'", "name='요요수진'")