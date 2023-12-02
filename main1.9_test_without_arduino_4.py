
def main_program():

    from Moving_Average import Moving_Average

    from timer_2 import Measure_Timer
    timer1 = Measure_Timer()

    from record_data import add_begining, get_new_program_start_row
    add_begining()
    new_program_start_row = get_new_program_start_row()
    print(new_program_start_row)


    moving_average_filter = Moving_Average(2)

    from coordinate_checker import CoordinateStore

    store = CoordinateStore()

    import cv2
    import numpy as np


    from save_load_cam_port import getCamPort

    cam_port = getCamPort()
    font = cv2.FONT_HERSHEY_SIMPLEX


    # Create a window and an image

    cv2.namedWindow("Ball_Tracker")

    # ADD Mouse Right Click To Remove The Last Point
    # Callback function for the mouse event


    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            pass

        if event == cv2.EVENT_RBUTTONDOWN and timer1.last_values:
            pass

    # Create a window and an image
    cv2.setMouseCallback("Ball_Tracker", mouse_callback)


    cap = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

    cap.set(3, 1280)
    cap.set(4, 720)

    # Get the camera frame size
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    lower_bound = np.array([30, 150, 50])
    upper_bound = np.array([255, 255, 180])



    while True:


        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_AREA)


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Use the mask to find contours in the frame
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        #add center line
        cv2.line(frame, (0,360), (1280,360), (0,177,0), 2)


        # Draw a circle around the largest contour
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))

            radius = int(radius)
            if radius > 5:

                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                cv2.circle(frame, center, 1, (0, 0, 255), 2)
                font_size = 1.2

                # Set the coordinates of the bottom-left corner
                center = moving_average_filter.getAvg(center)
                store.add_coordinate(center[0], center[1])
                if store.check_duplicate_coordinates():

                    cv2.putText(frame, f"NOT_MOVING", (10, 100), font, font_size, (0, 0, 255), 2)
                    ball_stop = 1

                else:
                    ball_stop = 0
                    cv2.putText(frame, f"BALL_MOVING", (10, 100), font, font_size, (0, 0, 255), 2)
                    global_data = 1

                orgin = (center[0], center[1])

                org = (center[0], center[1] + 100)

                # Write the text
                # cv2.putText(frame,f"{str(center[0])},{str(center[1])}", org, font, font_size, (255, 255, 255), 2)
                cv2.putText(frame, f"{str(center[0])},{str(center[1])}", org, font, font_size, (255, 255, 255), 2)

        cv2.imshow("Ball_Tracker", frame)

        key = cv2.waitKey(1)


        if key & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('Ball_Tracker', cv2.WND_PROP_VISIBLE) < 1:
            # Close the window and exit the program
            cv2.destroyAllWindows()
            break


    cap.release()





from open_files_and_folder import *
from tkinter import *
win= Tk()
win.title("Boccia Touchless Interface")
win.geometry("400x220")
left_frame = Frame(win, width=200, height=400, )
right_frame = Frame(win, width=650, height=400, )
right_frame2 = Frame(win, width=650, height=400, )
left_frame.grid(row=0, column=0, padx=10, pady=5)
right_frame.grid(row=0, column=1, padx=10, pady=5)
Label(right_frame, text="Arduino Code & Documentation").grid(row=0, column=0, padx=5, pady=5)
Button(right_frame, text ="Open Folder",command=open_source_code).grid(row=1, column=0, padx=5, pady=5)
Label(right_frame, text="Start Time Measuring Program").grid(row=2, column=0, padx=5, pady=5)
Button(right_frame, text ="Start Program",command=main_program).grid(row=3, column=0, padx=5, pady=5)
Label(right_frame, text="View Excel Data").grid(row=4, column=0, padx=5, pady=5)
Button(right_frame, text ="Open File",command=open_excel).grid(row=5, column=0, padx=5, pady=5)
Label(left_frame, text="Camera Port").grid(row=0, column=0, padx=5, pady=5)
Button(left_frame, text ="Edit Camera Port",command=open_cam_port).grid(row=1, column=0, padx=5, pady=5)
Label(left_frame, text="Arduino Com Port").grid(row=2, column=0, padx=5, pady=5)
Button(left_frame, text ="Edit Com Port",command=open_com_port,state="disabled").grid(row=3, column=0, padx=5, pady=5)
win.mainloop()
