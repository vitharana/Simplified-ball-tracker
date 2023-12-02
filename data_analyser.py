from moving_average import Moving_Average

mov_avg_filter = Moving_Average(2)


from motion_checker import Motion_Checker
ball_motion_checker = Motion_Checker(points_to_check=5)


from ball_timer import Measure_Timer
ball_timer = Measure_Timer()

import math



def update_ball_average(cv2):
    cv2.d_avg_coordinate = mov_avg_filter.getAvg(cv2.d_center)


def update_ball_motion_status(cv2):
    ball_motion_checker.add_coordinate(cv2.d_avg_coordinate)
    cv2.d_ball_mov = not ball_motion_checker.check_duplicate_coordinates()
    if cv2.d_center == (0,0):
        cv2.d_ball_mov = True


def run_timer_analyzer(cv2):

    if cv2.d_ball_mov:
        ball_timer.start_timer()
    
    if not cv2.d_ball_mov:
        ball_timer.stop_timer()

    cv2.d_ball_time = ball_timer.get_time_lapse(cv2)

    if cv2.d_key == '1':
        ball_timer.reset_timer()


def calculate_values(cv2):
    
    # Angle calculation

    (x_1, y_1) = cv2.d_initial_coordinate
    (x_2, y_2) = cv2.d_final_coordinate

    if cv2.d_ball_mov:
        (x_2, y_2) = cv2.d_avg_coordinate

    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

    

    try:
        cv2.d_ball_vel = distance / cv2.d_ball_time
    except:
        cv2.d_ball_vel = 0
    

    
    try:
        theta = (y_1 - y_2) / distance
    except:
        theta = 0

    if cv2.d_final_coordinate  == (-1,-1) and not cv2.d_ball_mov:
        theta = 0

    result_radians = math.asin(theta)
    # Convert radians to degrees if needed
    result_degrees = math.degrees(result_radians)
    cv2.d_ball_angle = result_degrees

    cv2.d_ball_dist = distance

    if cv2.d_final_coordinate == (-1,-1) and not cv2.d_ball_mov:
        cv2.d_ball_dist = 0
    

    



def save_data_point(cv2):

    cv2.d_data_points.append({
    'Initial_Coordinate': cv2.d_initial_coordinate,
    'Final_Coordinate': cv2.d_final_coordinate,
    'Time': cv2.d_ball_time,
    'Distance': cv2.d_ball_dist,
    'Angle': cv2.d_ball_angle

    })

def reset_values(cv2):
    cv2.all_data_ok = False
    cv2.d_radius = 0
    #cv2.d_center = (0, 0)
    #cv2.d_key = 'no_press'
    #cv2.d_hsv_state = False
    #cv2.d_data_table_state = False
    #cv2.d_avg_coordinate = (0,0)
    #cv2.d_ball_mov = True
    cv2.all_data_ok = False
    #cv2.d_initial_coordinate = (-1,-1)
    cv2.d_final_coordinate = (-1,-1)
    #cv2.d_radius_1 = 0
    cv2.d_radius_2 = 0
    cv2.d_ball_time = 0
    cv2.d_ball_angle = 0
    cv2.d_ball_dist = 0
    cv2.d_ball_vel = 0






def run_data_analyser(cv2):

    update_ball_average(cv2)
    update_ball_motion_status(cv2)
    run_timer_analyzer(cv2)

    
    if cv2.d_key == '1':

        print("1 pressed")
        cv2.d_initial_coordinate = cv2.d_avg_coordinate
        cv2.d_radius_1 = cv2.d_radius

        #Reset Values
        reset_values(cv2)    




    elif cv2.d_initial_coordinate != (-1,-1) and not cv2.d_ball_mov and cv2.d_ball_time > 0.3  :

        print("ready for the final coordinate")
        cv2.d_final_coordinate = cv2.d_avg_coordinate
        cv2.d_radius_2 = cv2.d_radius
        

    # aumatically calculate the values
    if cv2.d_initial_coordinate != (-1,-1) :
        calculate_values(cv2)


    if cv2.d_initial_coordinate != (-1,-1) and cv2.d_final_coordinate != (-1,-1) and cv2.d_ball_time > 0.3:
        cv2.all_data_ok = True
    











