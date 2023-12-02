from time import time


class Measure_Timer:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.time_lapse = 0
        self.timer_ticking = False

    def start_timer(self):
        if not self.timer_ticking:
            self.start_time = time()
            self.timer_ticking = True


    def stop_timer(self):
        if self.timer_ticking:
            self.stop_time = time()
        self.timer_ticking = False

    def get_time_lapse(self, cv2):
        if cv2.d_ball_mov:
            return (time() - self.start_time)
        else:
            t = self.stop_time - self.start_time
            if t > 0.2:
                return t
            else:
                return 0.0











