'''
face_recognition 라이브러리를 이용한 얼굴 인식
하지만 속도가 너무 느리다
'''
import cv2
import face_recognition

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()

    k = cv2.waitKey(10)

    if k == 27:
        break

    rgb_frame = frame[:, :, ::-1]

    face_location = face_recognition.face_locations(frame)

    for (top, right, bottom, left) in face_location:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


    cv2.imshow('Video', frame)

video.release()
cv2.destroyAllWindows()

