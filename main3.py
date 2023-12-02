import cv2
import numpy as np

#create the main window and sets the size
from initialize_opencv import create_main_window
main_window, cap = create_main_window(cv2)


#create the window for track bars
from trackbars import add_track_bars
add_track_bars(cv2)


while True:


    try:
        ret, frame = cap.read()
    except cv2.error as e:
        print(f"An error occurred: {e}")




    # Get current trackbar positions
    lower_h = cv2.getTrackbarPos("Lower H", "Trackbars")
    lower_s = cv2.getTrackbarPos("Lower S", "Trackbars")
    lower_v = cv2.getTrackbarPos("Lower V", "Trackbars")
    upper_h = cv2.getTrackbarPos("Upper H", "Trackbars")
    upper_s = cv2.getTrackbarPos("Upper S", "Trackbars")
    upper_v = cv2.getTrackbarPos("Upper V", "Trackbars")
    ker = cv2.getTrackbarPos("kernel", "Trackbars")
    blur = cv2.getTrackbarPos("blur", "Trackbars")
    radius_limit = cv2.getTrackbarPos("radius", "Trackbars")


    if blur > 0:
        try:
            frame = cv2.blur(frame, (blur, blur))
        except cv2.error as e:
            print(f"An error occurred: {e}")

    lower_bound = np.array([lower_h, lower_s, lower_v])
    upper_bound = np.array([upper_h, upper_s, upper_v])




    try:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    except cv2.error as e:
        print(f"An error occurred: {e}")





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

    # Display the main frame at the top
    cv2.imshow("Ball_Tracker", frame)

    # Create a black image to display trackbars at the bottom
    trackbar_image = np.zeros((150, frame.shape[1], 3), dtype=np.uint8)

    # Display trackbars on the black image
    cv2.putText(trackbar_image, "Press 'q' to quit", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(trackbar_image, "Adjustments:", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Show trackbars at the bottom
    cv2.imshow("Trackbars", trackbar_image)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
