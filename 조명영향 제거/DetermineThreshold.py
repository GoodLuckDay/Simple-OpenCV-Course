#Threshold 일정 이상 어두우면 검정색으로 일정 이상 밝으면 흰색으로 만든다.


import numpy as np
import cv2

def nothing(x):
    pass

def global_threshold():
    imgfile = "../images/document.jpg"
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    r = 600.0 / img.shape[0] #이미지의 가로 픽셀 수를 600으로 고정으로 고정하기 위해서 원래 이미지와 픽셀 사이즈 600의 비율을 구하고
    dim = (int(img.shape[1] * r) , 600) #세로 값에 그 비율 값을 곱하면서 사이즈를 생성 한다.
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    WindowName = "Window"
    TrackbarName = "Threshold"

    #트랙바를 생성을 하는 함수 생성하는 트랙바의 이름과 연결할 Window의 이름을 매개변수로 넘겨준다.
    #세번째 인자는 틑랙바의 초기값, 네번째 인자는 트랙바의 최대값을 의미한다. 마지막 인자는 트랙바가 움직였을때의 callback함수
    cv2.namedWindow(WindowName)
    cv2.createTrackbar(TrackbarName, WindowName, 50, 255, nothing)

    Threshold = np.zeros(img.shape, np.uint8) #Threshold를 적용한 이진값을 저장하는 2차원 배열

    while True:
        TrackbarPos = cv2.getTrackbarPos(TrackbarName, WindowName) #현재 트랙바의 위치를 반환하는 함수
        cv2.threshold(img, TrackbarPos, 255, cv2.THRESH_BINARY, Threshold) #thresholde를 적용시키는 함수이다. 맨 마지막 인자에 결과값이 적용된다.
        cv2.imshow(WindowName, Threshold)

        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break

if __name__ == "__main__":
    global_threshold()