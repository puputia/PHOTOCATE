# 특정 테이블의 특정 데이터를 검색

import pymysql

def select(tableName, column, searchCondition) :
    # 설명
    # tableName         => 검색하고자 하는 DB 테이블
    # column            => 검색하고자 하는 컬럼(select)
    # searchCondition   => 검색하고자 하는 데이터의 조건(where)
    # sqlSentence       => sql select 문 
    
    
    # DB 연결
    con = pymysql.connect(host='localhost', user='root', password='111111', db='capstone', charset='utf8', port=3305)
    cur = con.cursor()


    # print('DB 연결 성공')

    # print(tableName)
    # print(column)
    # print(searchCondition)

    # sqlSentence
    if searchCondition == 0 :
        sqlSentence = 'SELECT ' + column + ' FROM ' + tableName + ';'
    else :
        sqlSentence = 'SELECT ' + column + ' FROM ' + tableName + ' WHERE ' + searchCondition + ';'
    
    # print('sqlSentence : ', sqlSentence)

    # sql 실행
    cur.execute(sqlSentence)

    # 데이터 fetch
    rows = cur.fetchall()

    # 데이터 출력
    i = 0

    # return
    returnrows = []
    while(len(rows) > i) :
        # 괄호 & 쉼표 제거 후 저장
        testText = str(rows[i])
        # print('textText : ', testText)
        cleanrows = testText.translate({ord(letter): None for letter in "(,)'"})
        # print('i : ' + cleanrows)

        # 괄호 & 쉼표 & 따옴표 제거한 값을 띄어쓰기 단위로 나눠서 리스트에 저장(행이 바뀔 때는 값 사이에 '&' 값 삽입)
        # returnrows[i].append(for i in cleanrows.split())
        for a in cleanrows.split() :
            # print('celanrows.split() : ' + a)
            returnrows.append(a)

        # 행이 바뀌었음을 나타내줌(1차원 배열에서) 
        # returnrows.append('&')

        i+=1

    # db 연결 종료(return으로 값을 보내기 전에 해도 되는지 의문???????)
    con.close()

    return returnrows



# select 테스트
# print(select('trip', 'tname', "tname='바보'"))
# print(len(select('trip', 'tname', "tname='바보'")))