def key_press(cv2):

    # get the key pressed
    key = cv2.waitKey(1)


    if key & 0xFF == ord('q'):
        cv2.d_key = 'q' #quits the program


    elif key & 0xFF == ord('l'):
        cv2.d_key = 'l' # load detection profile

    elif key & 0xFF == ord('s'):
        cv2.d_key = 's' # save a detection profile

    elif key & 0xFF == ord('h'):
        #print("hsv mode") # Control the visibility of the HSV Mask Image

        cv2.d_hsv_state = not cv2.d_hsv_state
        if not cv2.d_hsv_state:
            cv2.destroyWindow("HSV")

    elif key & 0xFF == ord('t'):
    #print("hsv mode") # Control the visibility of the HSV Mask Image

        cv2.d_data_table_state = not cv2.d_data_table_state
        if not cv2.d_data_table_state:
            cv2.destroyWindow("Table_Window")

    elif key & 0xFF == ord('1'):
        cv2.d_key = '1' # for recording initial coordinates

    elif key & 0xFF == ord('d'):
        cv2.d_draw_illustration = not cv2.d_draw_illustration
        



    else:
        cv2.d_key = 'no_press'

