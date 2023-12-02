import cv2
import numpy as np

# Create two windows
window1_name = 'Window 1'
window2_name = 'Window 2'

cv2.namedWindow(window1_name)
cv2.namedWindow(window2_name)

# Set the initial position of the first window
window1_x, window1_y = 100, 100
cv2.moveWindow(window1_name, window1_x, window1_y)

while True:
    # Get the position of the first window
    _, _, width, height = cv2.getWindowImageRect(window1_name)
    window1_x, window1_y = cv2.getWindowImageRect(window1_name)[:2]

    # Set the position of the second window based on the first window
    window2_x = window1_x + width + 20  # Adjust the offset as needed
    window2_y = window1_y

    cv2.moveWindow(window2_name, window2_x, window2_y)

    # Create a black image for demonstration purposes
    image = np.zeros((300, 500, 3), dtype=np.uint8)

    # Display the image in both windows
    cv2.imshow(window1_name, image)
    cv2.imshow(window2_name, image)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()
