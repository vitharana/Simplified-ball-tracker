
import numpy as np

def show_data_table(cv2):
    cv2.namedWindow('Table_Window')
    data = [
        ("Ball Movement", cv2.d_ball_mov),
        ("Radius", cv2.d_radius),
        ("Center", cv2.d_center),
        ("Key", cv2.d_key),
        ("HSV State", cv2.d_hsv_state),
        ("Average Coordinate", cv2.d_avg_coordinate),
        ("All Data OK", cv2.all_data_ok),
        ("Initial Coordinate", cv2.d_initial_coordinate),
        ("Final Coordinate", cv2.d_final_coordinate),
        ("Radius 1", cv2.d_radius_1),
        ("Radius 2", cv2.d_radius_2),
        ("Ball Time", round(cv2.d_ball_time,4)),
        ("Ball Angle", round(cv2.d_ball_angle,4)),
        ("Ball Distance", round(cv2.d_ball_dist,4)),
        ("Ball Velocity", round(cv2.d_ball_vel,4)),
    ]

    # Create a black image with white text
    height = len(data) * 15 + 10
    width = 700
    table_img = 255 * np.ones((height, width, 3), dtype=np.uint8)

    # Define font and text color
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_thickness = 1
    text_color = (0, 0, 0)

    # Add text and lines
    for i, (key, value) in enumerate(data):
        x = 10 if i % 2 == 0 else width // 2 + 10
        y = (i // 2 + 1) * 20

        cv2.putText(table_img, f"{key}: ", (x, y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)
        cv2.putText(table_img, str(value), (x + 200, y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)

        # Draw a line between rows
        cv2.line(table_img, (0, y + 5), (width, y + 5), text_color, 1)

    cv2.imshow('Table_Window', table_img)
