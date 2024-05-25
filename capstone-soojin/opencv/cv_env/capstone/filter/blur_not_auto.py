# 참고 사이트 : https://yeko90.tistory.com/entry/opencv-how-to-use-selectroi
# 참고 사이트의 참고 사이트(selectROI 사용 방법) : https://yeko90.tistory.com/entry/opencv-how-to-use-selectroi

import cv2

img = cv2.imread('C:/Users/rlawn/opencv/cv_env/capstone/image/faceTest.jpg', cv2.IMREAD_COLOR)

# windowName = 윈도우 창 이름을 지정하는 부분
# 사용자가 특정 영역을 지정하면 거기에 해당하는 x, y, w, h 값을 리턴 받음
# x, y는 사각형 좌상단 좌표(x,y)
# w, h는 사각형의 width와 height를 의미
# showCrossshair = False : 이미지의 영역을 지정할 때 십자가를 표시할지 말지 결정하는 인자
x, y, w, h = cv2.selectROI(windowName='mosaic -> not auto', img=img, showCrosshair=False)

# print("x position, y posiiton : ", x, y)
# print("width, height : ", w, h)

# 선택한 구역의 이미지 픽셀값을 image_loc에 저장하고 blur 처리
# 커널 사이즈는 (50, 50)으로 처리
image_loc = img[y : y + h, x : x + w]
image_loc = cv2.blur(image_loc, (50, 50))

# blur 처리한 이미지를 원본의 동일 위치에 덧붙임
image_w_blur = img
image_w_blur[y : y + h, x : x + w] = image_loc

# selecROI 함수에 의해 출력된 그림파일을 없앰
cv2.destroyAllWindows()

# blur로 흐림처리된 이미지를 불러옴
image = image_w_blur
cv2.imshow("Blur", image)

# 선택한 영역만 보여줌(새로운 창으로)
# cropped_image = img[y : y + h, x : x + w]
# cv2.imshow("Cropped image", cropped_image)

# 필터 처리 후 이미지 저장
cv2.imwrite('C:/Users/rlawn/opencv/cv_env/capstone/image/after/blur_not_auto.jpg', image)

# 입력 무한 대기
cv2.waitKey(0)
cv2.destroyAllWindows()