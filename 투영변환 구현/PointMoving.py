import numpy as np
import cv2

#임의의 점을 옮기면 다른 점들도 같이 이동을 한다.

def warfAffline():
    img = cv2.imread("../images/transform.png")

    pts1 = np.float32([[50, 50], [200, 50], [20, 200]]) #옮기고자 하는 점들
    pts2 = np.float32([[70, 100], [220, 50], [150, 250]]) #옮기고자 하는 위치

    M = cv2.getAffineTransform(pts1, pts2)

    result = cv2.warpAffine(img, M, (350, 300)) #원근 보정 X

    cv2.imshow('original', img)
    cv2.imshow('Affline Transform', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__ == "__main__":
    warfAffline()