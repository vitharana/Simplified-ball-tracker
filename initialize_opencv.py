def create_main_window(cv2):
    #cap = cv2.VideoCapture(3, cv2.CAP_DSHOW)
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Create windows
    cv2.namedWindow(cv2.Window1_Name_Ball_Tracker, cv2.WINDOW_NORMAL)
    cv2.namedWindow(cv2.Window2_Name_Track_Bars, cv2.WINDOW_NORMAL)
    

    cv2.resizeWindow(cv2.Window1_Name_Ball_Tracker, 1280, 720)
    

    return cap



