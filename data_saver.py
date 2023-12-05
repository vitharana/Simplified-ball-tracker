from pandas_to_excel import Data_Saver
pd_data_saver = Data_Saver()


def save_data_point(cv2):
    if cv2.d_record_data and cv2.all_data_ok:

        cv2.d_data_points.append({
            'Index': cv2.d_data_point_count,
            'Initial_Coordinate': cv2.d_initial_coordinate,
            'Initial_Coordinate':  cv2.d_initial_coordinate,
            'Final_Coordinate': cv2.d_final_coordinate,
            'Distance': round(cv2.d_ball_dist, 4),
            'Time': round(cv2.d_ball_time, 4),
            'Velocity': round(cv2.d_ball_vel, 4),
            'Angle': round(cv2.d_ball_angle, 4),
        })


        print(cv2.d_data_points[-1])
        pd_data_saver.export_data(cv2)
        cv2.d_data_point_count += 1
        cv2.d_record_data = False





