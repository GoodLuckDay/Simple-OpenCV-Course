import cv2
import face_recognition

video_capture = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier()
face_cascade.load("../venv/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml")

while(True):
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 3, 0, (30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3, 4, 0)

    cv2.imshow('Face', frame)

    k = cv2.waitKey(10)

    if k == 27:
        break

video_capture.release()
cv2.destroyAllWindows()