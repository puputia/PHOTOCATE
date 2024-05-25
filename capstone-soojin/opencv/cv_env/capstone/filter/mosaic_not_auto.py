# 참고 사이트 : https://ponyozzang.tistory.com/598

import cv2

src = cv2.imread('C:/Users/rlawn/opencv/cv_env/capstone/image/faceTest.jpg', cv2.IMREAD_COLOR)
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst


# windowName = 윈도우 창 이름을 지정하는 부분
# 사용자가 특정 영역을 지정하면 거기에 해당하는 x, y, w, h 값을 리턴 받음
# x, y는 사각형 좌상단 좌표(x,y)
# w, h는 사각형의 width와 height를 의미
# showCrossshair = False : 이미지의 영역을 지정할 때 십자가를 표시할지 말지 결정하는 인자
x, y, w, h = cv2.selectROI(windowName='mosaic -> not auto', img=src, showCrosshair=False)

dst_area = mosaic_area(src, x, y, w, h)

# selecROI 함수에 의해 출력된 그림파일을 없앰
cv2.destroyAllWindows()

# 모자이크 된 이미지 출력
cv2.imshow('mosaic not auto', dst_area)
cv2.waitKey(0)

# 모자이크 된 이미지 저장
cv2.imwrite('C:/Users/rlawn/opencv/cv_env/capstone/image/after/mosaic_not_auto.jpg', dst_area)