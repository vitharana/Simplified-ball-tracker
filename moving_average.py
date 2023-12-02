class Moving_Average:
    def __init__(self, n=5):
        self.data_bufferx = []
        self.data_buffery = []
        self.window_size = n

    def getAvg(self, coordinate):

        datax = coordinate[0]
        datay = coordinate[1]

        self.data_bufferx.append(datax)
        if len(self.data_bufferx) > self.window_size:
            self.data_bufferx.pop(0)

        self.data_buffery.append(datay)
        if len(self.data_buffery) > self.window_size:
            self.data_buffery.pop(0)

        return int(sum(self.data_bufferx) / len(self.data_bufferx)), int(sum(self.data_buffery) / len(self.data_buffery))
        #return sum(self.data_bufferx) / len(self.data_bufferx), sum(self.data_buffery) / len(self.data_buffery)







