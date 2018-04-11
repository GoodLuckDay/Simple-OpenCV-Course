import numpy as np
import cv2
from matplotlib import pyplot as plt

def contour():
    imgfile = "../images/Test1.jpg"
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #원본 이미지와 흑백이미지가 따로 존재

    edge = cv2.Canny(imgray, 100, 200) #Canny 알고리즘을 이용하여 이미지의 edge를 검출한다.
    image,contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#이미지의 모든 외곽을 검출한다. 입력변수로 흑백이미지, 생성이 되어질 계층구조 어떤식으로 외곽선을 만들지를 준다.

    cv2.imshow('edge', edge)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1) #src에 윤곽선을 그리는 함수 3번째 인자는 윤곽선의 인덱스 4번째는 색깔 5번쨰는 색깔을 가리킨다.
    cv2.imshow('image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__ == "__main__":
    contour()