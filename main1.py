import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

cap.set(3, 1280)
cap.set(4, 720)

cv2.namedWindow("Color Adjustments", cv2.WINDOW_NORMAL)

# Initialize trackbars for lower and upper bounds
cv2.createTrackbar("Lower H", "Color Adjustments", 28, 255, nothing)
cv2.createTrackbar("Lower S", "Color Adjustments", 113, 255, nothing)
cv2.createTrackbar("Lower V", "Color Adjustments", 45, 255, nothing)
cv2.createTrackbar("Upper H", "Color Adjustments", 120, 255, nothing)
cv2.createTrackbar("Upper S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper V", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("kernel", "Color Adjustments", 38, 255, nothing)
cv2.createTrackbar("blur", "Color Adjustments", 1, 10, nothing)
cv2.createTrackbar("radius", "Color Adjustments", 5, 100, nothing)

while True:
    ret, frame = cap.read()

    # Get current trackbar positions
    lower_h = cv2.getTrackbarPos("Lower H", "Color Adjustments")
    lower_s = cv2.getTrackbarPos("Lower S", "Color Adjustments")
    lower_v = cv2.getTrackbarPos("Lower V", "Color Adjustments")
    upper_h = cv2.getTrackbarPos("Upper H", "Color Adjustments")
    upper_s = cv2.getTrackbarPos("Upper S", "Color Adjustments")
    upper_v = cv2.getTrackbarPos("Upper V", "Color Adjustments")
    ker = cv2.getTrackbarPos("kernel", "Color Adjustments")
    blur = cv2.getTrackbarPos("blur", "Color Adjustments")
    radius_limit = cv2.getTrackbarPos("blur", "Color Adjustments")

    frame = cv2.blur(frame, (blur, blur))

    lower_bound = np.array([lower_h, lower_s, lower_v])
    upper_bound = np.array([upper_h, upper_s, upper_v])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    kernel = np.ones((ker, ker), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Hsv", mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (0, 360), (1280, 360), (0, 177, 0), 2)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))

        radius = int(radius)
        if radius > radius_limit:
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.circle(frame, center, 1, (0, 0, 255), 2)

    cv2.imshow("Ball_Tracker", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
