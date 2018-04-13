#이전에는 TrackBar의 값으로 Threshold 값을 적용시켰지만 주변 픽셀의 값을 이용하여 Threshold를 적용

import numpy as np
import cv2

def adaptive_threshold():
    imgfile = "../images/document2.jpg"
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    r = 600.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 600)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    blur = cv2.GaussianBlur(img, (5,5), 0) #주변 픽셀의 평균값을 대입함으로서 이미지를 흐릿하게 만든다. 2번째 인자는 주변 픽셀의 크기 크면 클수록 정도가 커진다.
    #이진화를 하기전 blur 효과를 줌으로서 noise를 제거

    result_without_blur = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10) #마지막 인자는 주변 픽셀에서 뺴는 상수 값
    result_with_blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

    cv2.imshow('Without Blur', result_without_blur)
    cv2.imshow('With Blur', result_with_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
if __name__ == "__main__":
    adaptive_threshold()