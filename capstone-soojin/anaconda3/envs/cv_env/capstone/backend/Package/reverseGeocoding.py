# 역지오코딩
# https://parkgihyeon.github.io/project/geocoding-api/#%EA%B0%9C%EC%9D%B8-key-%EB%B0%9C%EA%B8%89%EB%B0%9B%EA%B8%B0
# https://parkgihyeon.github.io/project/geocoding-api/#1-%EC%A7%80%EC%98%A4%EC%BD%94%EB%94%A9-%EC%A3%BC%EC%86%8C%EB%A5%BC-%ED%86%B5%ED%95%B4-%EC%9C%84%EB%8F%84-%EA%B2%BD%EB%8F%84-%EC%A2%8C%ED%91%9C-%EC%96%BB%EA%B8%B0



# 역지오코딩
# 결과 설명 페이지 : https://developers.kakao.com/docs/latest/ko/local/dev-guide
import requests, json, pprint

# from os import path
# # 현재 위치
# print(path.abspath('.'))
# # 상위 폴더 위치
# print(path.abspath('..'))

# import sys
# print(sys.path)

def get_address(lat, lng):
    lat = str(lat)
    lng = str(lng)

    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x="+lng+"&y="+lat
    # 'KaKaoAK '는 그대로 두시고 개인키만 지우고 입력해 주세요.
    # ex) KakaoAK 6af8d4826f0e56c54bc794fa8a294
    headers = {"Authorization": "KakaoAK 09b135616cad979948bcb30f293900cf"}
    api_json = requests.get(url, headers=headers)
    full_address = json.loads(api_json.text)

    # 변수값 선언 및 초기화(gps_1 : 00시, gps_2 : 00구)
    gps_1 = ''
    gps_2 = ''

    # 주소 모음(fullAddress = 00시/00구 정보 + 필요 없는 정보들을 딕셔너리 형태로 저장)
    fullAddress = full_address['documents'][0]
    # print(fullAddress)

    # 변수 값 삽입
    gps_1 = fullAddress.pop('region_1depth_name')
    gps_2 = fullAddress.pop('region_2depth_name')
    # print('gps_1 : ', gps_1)
    # print('gps_2 : ', gps_2)

    # 딕셔너리 형태로 저장
    gpsDic = {'gps_1' : gps_1, 'gps_2' : gps_2}

    return gpsDic

# full_address = get_address('37.294479699722224', '127.20538879972223')
# pprint.pprint(full_address)