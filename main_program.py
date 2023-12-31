from handle_keys import key_press
from trackbars import get_trackbar_values
import numpy as np
import  os

def save_screenshot(cv2,frame):
    if cv2.d_key == 'r' and cv2.d_data_point_count > 0:
        folder_name = f"Data Folder_{cv2.d_folder_no}"
        filename = os.path.join(folder_name, f"{cv2.d_data_point_count-1}.jpg")
        cv2.imwrite(filename, frame)





def draw_illustration(cv2,frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1.0

    if cv2.d_draw_illustration:

        cv2.putText(frame, f"(0,0)", (10, 30), font, font_size, (0, 0, 0), 2)
        cv2.putText(frame, f"(1280,720)", (1100, 700), font, font_size, (0, 0, 0), 2)

        cv2.putText(frame, f"Initial Point: {cv2.d_initial_coordinate}", (800, 100), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Initial Point: {cv2.d_initial_coordinate}", (800, 100), font, font_size, (0, 255, 255), 1)

        cv2.putText(frame, f"Final Point: {cv2.d_final_coordinate}", (800, 150), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Final Point: {cv2.d_final_coordinate}", (800, 150), font, font_size, (0, 255, 255), 1)

        cv2.putText(frame, f"Time: {round(cv2.d_ball_time, 4)}", (800, 200), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Time: {round(cv2.d_ball_time, 4)}", (800, 200), font, font_size, (0, 255, 255), 1)

        cv2.putText(frame, f"Distance: {round(cv2.d_ball_dist, 4)}", (800, 250), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Distance: {round(cv2.d_ball_dist, 4)}", (800, 250), font, font_size, (0, 255, 255), 1)


        cv2.putText(frame, f"Angle: {round(cv2.d_ball_angle, 4)}", (800, 300), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Angle: {round(cv2.d_ball_angle, 4)}", (800, 300), font, font_size, (0, 255, 255), 1)

        cv2.putText(frame, f"Velocity: {round(cv2.d_ball_vel, 4)}", (800, 350), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Velocity: {round(cv2.d_ball_vel, 4)}", (800, 350), font, font_size, (0, 255, 255), 1)

        cv2.putText(frame, f"Data Index: {cv2.d_data_point_count}", (800, 400), font, font_size, (0, 0, 0), 4)
        cv2.putText(frame, f"Data Index: {cv2.d_data_point_count}", (800, 400), font, font_size, (0, 255, 255), 1)

        if cv2.d_avg_coordinate != (0,0) and cv2.d_initial_coordinate != (-1,-1):
            cv2.line(frame, cv2.d_initial_coordinate, cv2.d_avg_coordinate, (0, 177, 255), 2)

        if cv2.d_initial_coordinate != (0, 0) or cv2.d_initial_coordinate != (-1, -1):
            cv2.circle(frame, cv2.d_initial_coordinate, cv2.d_radius_1, (0, 0, 255), 2)
            cv2.circle(frame, cv2.d_initial_coordinate, 1, (0, 0, 255), 2)







def run_main_program(cv2, cap):

    radius = 0
    center = (0, 0)

    try:
        ret, frame = cap.read()
    except cv2.error as e:
        print(f"An error occurred: {e}")

    # to flip the camera frame
    #frame = cv2.flip(frame, -1)



    # Get current trackbar positions

    lower_h, upper_h, lower_s, upper_s, lower_v, upper_v, ker, blur, radius_limit = get_trackbar_values(cv2)

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


    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #get image size & draw center line
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    #print(frame_height,frame_width)
    cv2.line(frame, (0, int(frame_height/2)), (frame_width, int(frame_height/2)), (0, 177, 0), 2)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))

        radius = int(radius)
        if radius > radius_limit:
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.circle(frame, center, 1, (0, 0, 255), 2)

            cv2.circle(mask, center, radius, (255, 255, 255), 2)
            cv2.circle(mask, center, 3, (0, 0, 0), 5)


    # Display the main frame at the top

    draw_illustration(cv2, frame)

    cv2.imshow(cv2.Window1_Name_Ball_Tracker, frame)
    
    if cv2.d_hsv_state:
        cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)

        cv2.resizeWindow("HSV", 360*2, 360*1)
        #print("Execute the hsv")
        cv2.imshow("HSV", mask)

    # update the key press
    key_press(cv2)

    # Save screen shot when r is pressed

    save_screenshot(cv2, frame)

    # update the ball data
    cv2.d_radius = radius
    cv2.d_center = center

    

