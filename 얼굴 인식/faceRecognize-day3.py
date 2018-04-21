'''
프레임의 크기를 작게 한 후 연산을 함으로써 속도를 향상을 시켰다.
'''

import cv2
import face_recognition

video = cv2.VideoCapture(0)
face_locations = []
while True :
    ret, frame = video.read()

    if not ret:
        break

    k = cv2.waitKey(10)

    if k == 27:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    for (top, right, bottom, left) in face_locations:
        top *= 4
        right *=4
        bottom *=4
        left *=4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

video.release()
cv2.destroyAllWindows()