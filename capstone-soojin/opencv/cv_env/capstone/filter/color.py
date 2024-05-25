import cv2
import numpy as np

src = cv2.imread('image/testimg.jpg')
dst = cv2.imread('image/testimg.jpg')

cv2.imshow('src', src)
# cv2.imshow('dst',dst)

output = dst.copy()

#lab로 변환
srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst,cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output,cv2.COLOR_BGR2LAB)

srcLab = srcLab.astype('float')
dstLab = dstLab.astype('float')
outputLab = outputLab.astype('float')

print(srcLab)

#채널 분리
srcL, srcA,srcB = cv2.split(srcLab)
dstL,dstA,dstB =cv2.split(dstLab)
outputL,outputA,outputB = cv2.split(outputLab)

#색 바꾸기
outputL = dstL-dstL.mean()
outputA = dstA-dstA.mean()
outputB = dstB-dstB.mean()

outputL = outputL+srcL.mean()
outputA = outputA+srcA.mean()
outputB = outputB+srcB.mean()

#얻고자 하는 이미지
outL = (outputL*srcL.std() / dstL.std())
outA = (outputA*srcA.std() / dstA.std())
outB = (outputB*srcB.std() / dstB.std())

#눈으로 보기위한 코드? 사진은 0~255 사이값으로 세팅
outL = np.clip(outL,0,255)
outA = np.clip(outA,0,255)
outB = np.clip(outB,0,255)

#채널 합치기
outputLab = cv2.merge([outL, outA, outB])

#이미지는 정수. 위의 작업은 float이므로 형 변환 실행
outputLab = np.uint8(outputLab)

#imshow는 BGR이므로 바꿔준다.
outLab = cv2.cvtColor(outputLab, cv2.COLOR_LAB2BGR)

cv2.imshow('outLab', outLab)

# 처리한 이미지 저장 -> 저장이 안됨...........
cv2.imwrite('image/after/color.jpg', outLab)


cv2.waitKey(0)
cv2.destroyAllWindows()