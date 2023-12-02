import cv2

cv2.Window1_Name_Ball_Tracker = 'Ball_Tracker'
cv2.Window2_Name_Track_Bars = 'Track_Bars'



# main data
cv2.d_radius = 0
cv2.d_center = (0, 0)
cv2.d_key = 'no_press'
cv2.d_hsv_state = False
cv2.d_avg_coordinate = (0,0)
cv2.d_ball_mov = True
cv2.all_data_ok = False





#Data_Saved
cv2.d_initial_coordinate = (-1,-1)
cv2.d_final_coordinate = (-1,-1)
cv2.d_radius_1 = 0
cv2.d_radius_2 = 0
cv2.d_ball_time = 0
cv2.d_ball_angle = 0
cv2.d_ball_dist = 0
cv2.d_ball_vel = 0


cv2.d_data_points = []



# create the main window and sets the size
from initialize_opencv import create_main_window

cap = create_main_window(cv2)

# create the window for track bars
from trackbars import add_track_bars

add_track_bars(cv2)


from main_program import run_main_program

# load the files
from trackbars import load_trackbar_values, save_trackbar_values

#ball analyser functions
from data_analyser import run_data_analyser



from display_current_data import show_data_table

while True:

    # lock windows


    run_main_program(cv2, cap)
    run_data_analyser(cv2)
    #print(cv2.d_avg_coordinate, cv2.d_ball_mov, cv2.d_ball_time)

    print(f"current: {cv2.d_avg_coordinate}, initial: {cv2.d_initial_coordinate}, r1: {cv2.d_radius_1}, t1: {cv2.d_ball_time}, final: {cv2.d_final_coordinate}, r2: {cv2.d_radius_2} angle: {cv2.d_ball_angle}, vel: {cv2.d_ball_vel}")

    #print(cv2.d_data_points if len(cv2.d_data_points) > 0 else "")

    #print(cv2.d_key, cv2.d_radius, cv2.d_center)

    # quit the program
    if cv2.d_key == 'q':
        break

    # load saved profile
    elif cv2.d_key == 'l':
        load_trackbar_values(cv2)

    # save detection profile
    elif cv2.d_key == 's':
        save_trackbar_values(cv2)

    show_data_table(cv2)

    




# End the resources allocated
cap.release()
cv2.destroyAllWindows()
