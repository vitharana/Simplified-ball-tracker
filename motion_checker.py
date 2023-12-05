class Motion_Checker:
    def __init__(self,points_to_check = 5):
        self.points_to_check = points_to_check
        self.coordinates = []

    def add_coordinate(self, center):
        self.coordinates.append(center)
        if len(self.coordinates) > self.points_to_check:
            self.coordinates.pop(0)

    def check_duplicate_coordinates(self):
        for i in range(len(self.coordinates)):
            for j in range(i + 1, len(self.coordinates)):
                if self.coordinates[i] == self.coordinates[j]:
                    return True
        return False
