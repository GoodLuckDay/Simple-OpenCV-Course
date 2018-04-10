"""
이미지를 흑백으로 읽어와서 저장을 하는 파이썬 코드이다.
imread() 함수의 인자로는 이미지 파일의 경로와 이미지를 흑백, 컬러등의 색깔로 읽는것을 결정 할수 있다.
namedWindow() 함수를 이용해서 속성 부가 가능 WINDOW_NORMAL을 이용하여 보통 크기의 WiNDOW를 보여준다.
imshow() 함수는 해당 image객체를 생성 한것을 보여주는 역활
waitKey()함수는 키보드 입력을 기다리는 함수이다. 0이면 키보드 입력을 무한히 기다린다. 반환값은 입력한 키보드 문자의 아스키 코드값이다.
imwrite() 함수를 이용하여 이지미를 저장 가능
"""
import numpy as np
import cv2

def handle_image():
    imgfile = '../images/Test1.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    elif k == ord('s'):
        cv2.imwrite('grayImage.png', img)
        cv2.destroyAllWindows()
        cv2.waitKey(1)



if __name__ == '__main__':
    handle_image()