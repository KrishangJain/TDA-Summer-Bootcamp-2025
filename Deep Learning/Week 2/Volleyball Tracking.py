import cv2 as cv
import numpy as np

cap = cv.VideoCapture("C:/Users/kresh/OneDrive/Desktop/Coding/repos/TDA-Summer-Bootcamp-2025/Deep Learning/Week 2/volleyball.mp4")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    yellow_low = np.array([20, 100, 100])
    yellow_high = np.array([35, 255, 255])
    blue_low = np.array([100, 150, 0])
    blue_high = np.array([130, 255, 255])
    red_low = np.array([0, 100, 100])
    red_high = np.array([10, 255, 255])

    mask_yellow = cv.inRange(hsv, yellow_low, yellow_high)
    mask_blue = cv.inRange(hsv, blue_low, blue_high)
    mask_red = cv.inRange(hsv, red_low, red_high)

    ball_mask = cv.bitwise_or(mask_yellow, mask_blue)
    contours, _ = cv.findContours(ball_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv.contourArea(c)
        if area > 50 and area < 300:
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    red_count = 0
    red_contours, _ = cv.findContours(mask_red, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in red_contours:
        if cv.contourArea(c) > 500:
            red_count = red_count + 1

    yellow_count = 0
    yellow_contours, _ = cv.findContours(mask_yellow, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in yellow_contours:
        if cv.contourArea(c) > 500:
            yellow_count = yellow_count + 1

    cv.putText(frame, "Red: " + str(red_count), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv.putText(frame, "Yellow: " + str(yellow_count), (10, 60), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
