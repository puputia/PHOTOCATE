# 참고 사이트 : https://data-make.tistory.com/170
# 입력창 생성 참고 사이트 : https://yeachan.tistory.com/6
import os
import pymysql
# import pandas as pd
from . import DB_insert as insert
from . import DB_select as select


def creatFolder(directory):
    try : 
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.' + directory)

# getImage.py 에서 사용하는 mkdir
def mkdir(sharFoldername, owner, startday, finishday) :
    # 설명
    # tname -> 사용자에게 입력받은 공유폴더명!

    # offical_trip_url : 공유폴더를 생성할 상위공간
    offical_trip_url = 'C:/Users/Photocate'

    # 사용자가 지정한 공유 폴더 이름
    tname = sharFoldername
    trip_url = offical_trip_url + '/' + tname
    creatFolder(trip_url)


    # DB에 저장하기
    # 설명
    # owner     => user_id(공유폴더를 처음 만든 사람)
    # tname     => 공유폴더 이름(사용자 지정)

    insert.insert('trip', '(trip_url, owner, tname, startday, finishday)', f"('{trip_url}', '{owner}', '{tname}', '{startday}', '{finishday}')")


# filter.py 에서 사용하는 mkdir
# 사용자 폴더 생성(필터 처리 진행 전에 무조건 1회 실행) => 필터 처리 된 이미지를 저장할 예정
def filtermkdir(shareFolder, user, shareFolderName) :
    # 설명
    # shareFolder       => 처리할 이미지의 경로
    # user              => 처리를 주도하고 있는 사용자 id
    # selectUSER        => 입력 매개변수로 넘겨받은 사용자 id가 db에 저장된 정보가 맞는지 확인
    # shareFolderName   => 공유폴더 이름
    # checkfolderURL    => 사용자 폴더가 있는지 경로로 확인
    # checkcheck        => C:/Photocata/공유폴더 경로
    # userFolder        => 처리된 이미지가 저장될 경로(공유폴더 > 사용자 폴더)

    # 경로에 슬래쉬 정리
    shareFolder = shareFolder.replace('\\', '/')

    # 사용자 id 확인
    selectUSER = select.select('user', 'user_id', f"user_id='{user}'")
    if len(selectUSER) == 1 :
        user = selectUSER[0]
    elif len(selectUSER) > 1 :
        return "select : user_id error : 사용자 아이디가 너무 많습니다."
    elif len(selectUSER) == 0 :
        return "select : user_id error : 사용자 아이디가 존재하지 않습니다."
    # C:/Users/Photocate/사용자 폴더
    global userFolder

    # 공유 폴더 하위에 유저 이름의 폴더가 있는지 확인
    correctURL = 'C:/Users/Photocate' + '/' + shareFolderName
    checkfolderURL = shareFolder.rsplit('/')
    global checkcheck

    i = 0
    for a in checkfolderURL :
        if a == shareFolderName :
            checkcheck = '/'.join(checkfolderURL[0:i+1])
            if checkcheck == correctURL :
                # C:/Users/Photocate 하위에 존재하는 이미지이다.
                if checkfolderURL[i+1] == f'{user}' :
                    # C:/Users/Photocate/사용자 폴더까지 만들어진 상태
                    userFolder = shareFolder.rsplit('/', 1)[0]
                    # print("폴더 안 만들고 처리시작하기")
                    return userFolder
                elif checkfolderURL[i+1] == checkfolderURL[len(checkfolderURL)-1] :
                    # C:/Users/Photocate/이미지 파일 -> 사용자 폴더는 안 만들어짐
                    userFolder = shareFolder.rsplit('/', 1)[0] + '/' + user
                    # print("사용자 폴더 만들고 처리 시작하기")
                    creatFolder(userFolder)
                    return userFolder
                else :
                    return "해당 이미지를 처리할 수 있는 위치가 아닙니다. 다시 한 번 확인해 주세요."
            else :
                return "현재 이미지는 공유폴더 하위에 위치하지 않습니다. 다시 한 번 확인해 주세요."
        else :
            i+=1

    # # a = len(checkfolderURL) - 1
    # for i in checkfolderURL :
    #     if(i != shareFolderName) :
    #         a-=1
    #     else :
    #         # rsplit의 2번째가 공유 폴더 이름과 같다면, 해당 이미지는 필터 처리 된 적 없는 이미지임
    #         userFolder = shareFolder.rsplit('/', 1)[0] + '/' + user

    #     print("이미지 저장 경로(check1) : ", userFolder)

    #     # 만약, 공유 폴더 하위에 유저 이름의 폴더가 있으면 폴더를 안 만들고, 없으면 만들기.
    #     try :
    #         if not os.path.exists(userFolder) :
    #             os.makedirs(userFolder)
    #             print("공유 폴더 하위에 사용자 폴더가 없어서 만들었어요!")
    #         else :
    #             print("공유 폴더 하위에 사용자 폴더가 있어서 안 만들었어요!")
            
    #         # 공유 폴더 하위에 사용자 폴더 경로 return
    #         return userFolder
        
    #     except OSError :
    #         print("Error : Creating directory." + userFolder)

    # elif(checkfolderURL[1] == user) :
    #     # rsplit의 2번쨰가 유저 이름과 같다면, 해당 이미지는 필터 처리 된 적 있는 이미지임
    #     userFolder = checkfolderURL[0] + '/' + checkfolderURL[1]
    #     print("이미지 저장 경로(check2) : ", userFolder)
    #     return userFolder

