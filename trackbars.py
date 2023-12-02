from detection_parameters import write_default_values_file, get_values_from_file, write_custom_values_file
def add_track_bars(cv2):

    write_default_values_file()
    data = {
        'lower_h': 28,
        'upper_h': 120,
        'lower_s': 30,
        'upper_s': 255,
        'lower_v': 45,
        'upper_v': 255,
        'kernel': 20,
        'blur': 0,
        'radius': 5
    }

    def nothing(x):
        pass
    #cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)
    cv2.resizeWindow(cv2.Window2_Name_Track_Bars, 600, 240)

    # Create trackbars for lower and upper bounds
    cv2.createTrackbar("Lower H", cv2.Window2_Name_Track_Bars, data['lower_h'], 255, nothing)
    cv2.createTrackbar("Upper H", cv2.Window2_Name_Track_Bars, data['upper_h'], 255, nothing)
    cv2.createTrackbar("Lower S", cv2.Window2_Name_Track_Bars, data['lower_s'], 255, nothing)
    cv2.createTrackbar("Upper S", cv2.Window2_Name_Track_Bars, data['upper_s'], 255, nothing)
    cv2.createTrackbar("Lower V", cv2.Window2_Name_Track_Bars, data['lower_v'], 255, nothing)
    cv2.createTrackbar("Upper V", cv2.Window2_Name_Track_Bars, data['upper_v'], 255, nothing)
    cv2.createTrackbar("Kernel", cv2.Window2_Name_Track_Bars, data['kernel'], 255, nothing)
    cv2.createTrackbar("Blur", cv2.Window2_Name_Track_Bars, data['blur'], 10, nothing)
    cv2.createTrackbar("Radius",cv2.Window2_Name_Track_Bars, data['radius'], 100, nothing)

def get_trackbar_values(cv2):

    lower_h = cv2.getTrackbarPos("Lower H", cv2.Window2_Name_Track_Bars)
    upper_h = cv2.getTrackbarPos("Upper H", cv2.Window2_Name_Track_Bars)
    lower_s = cv2.getTrackbarPos("Lower S", cv2.Window2_Name_Track_Bars)
    upper_s = cv2.getTrackbarPos("Upper S", cv2.Window2_Name_Track_Bars)
    lower_v = cv2.getTrackbarPos("Lower V", cv2.Window2_Name_Track_Bars)
    upper_v = cv2.getTrackbarPos("Upper V", cv2.Window2_Name_Track_Bars)
    ker = cv2.getTrackbarPos("Kernel", cv2.Window2_Name_Track_Bars)
    blur = cv2.getTrackbarPos("Blur", cv2.Window2_Name_Track_Bars)
    radius_limit = cv2.getTrackbarPos("Radius", cv2.Window2_Name_Track_Bars)


    data = (lower_h, upper_h, lower_s, upper_s, lower_v, upper_v, ker, blur, radius_limit)

    return data

def load_trackbar_values(cv2):

    data = get_values_from_file()

    cv2.setTrackbarPos("Lower H", cv2.Window2_Name_Track_Bars,data['lower_h'])
    cv2.setTrackbarPos("Upper H", cv2.Window2_Name_Track_Bars,data['upper_h'])
    cv2.setTrackbarPos("Lower S", cv2.Window2_Name_Track_Bars,data['lower_s'])
    cv2.setTrackbarPos("Upper S", cv2.Window2_Name_Track_Bars,data['upper_s'])
    cv2.setTrackbarPos("Lower V", cv2.Window2_Name_Track_Bars,data['lower_v'])
    cv2.setTrackbarPos("Upper V", cv2.Window2_Name_Track_Bars,data['upper_v'])
    cv2.setTrackbarPos("Kernel", cv2.Window2_Name_Track_Bars,data['kernel'])
    cv2.setTrackbarPos("Blur", cv2.Window2_Name_Track_Bars,data['blur'])
    cv2.setTrackbarPos("Radius", cv2.Window2_Name_Track_Bars,data['radius'])

def save_trackbar_values(cv2):
    lower_h, upper_h, lower_s, upper_s, lower_v, upper_v, ker, blur, radius_limit = get_trackbar_values(cv2)

    data = {
        'lower_h': lower_h,
        'upper_h': upper_h,
        'lower_s': lower_s,
        'upper_s': upper_s,
        'lower_v': lower_v,
        'upper_v': upper_v,
        'kernel': ker,
        'blur': blur,
        'radius': radius_limit
    }

    write_custom_values_file(data)