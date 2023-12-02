




def lock_windows(cv2):
    window1_x, window1_y = 100, 100

    cv2.moveWindow(cv2.Window1_Name_Ball_Tracker, window1_x, window1_y)

    _, _, width, height = cv2.getWindowImageRect(cv2.Window1_Name_Ball_Tracker)
    window1_x, window1_y = cv2.getWindowImageRect(cv2.Window2_Name_Track_Bars)[:2]

    # Set the position of the second window based on the first window
    window2_x = window1_x + width + 20  # Adjust the offset as needed
    window2_y = window1_y

    cv2.moveWindow(cv2.Window2_Name_Track_Bars, window2_x, window2_y)