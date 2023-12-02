import cv2

# main data
cv2.d_radius = 0
cv2.d_center = (0, 0)
cv2.d_key = 'no_press'


# create the main window and sets the size
from initialize_opencv import create_main_window

main_window, cap = create_main_window(cv2)

# create the window for track bars
from trackbars import add_track_bars

add_track_bars(cv2)


from main_program import run_main_program

# load the files
from trackbars import load_trackbar_values, save_trackbar_values

while True:

    run_main_program(cv2, cap, hsv_show=False)

    print(cv2.d_key, cv2.d_radius, cv2.d_center)

    # quit the program
    if cv2.d_key == 'q':
        break

    # load saved profile
    elif cv2.d_key == 'l':
        load_trackbar_values(cv2)

    # save detection profile
    elif cv2.d_key == 's':
        save_trackbar_values(cv2)




# End the resources allocated
cap.release()
cv2.destroyAllWindows()
