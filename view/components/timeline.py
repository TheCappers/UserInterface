
class Timeline:
    def __init__(self):
        self.data_range = ''
        self.timeline_tile = ''
        self.time_unit = ''
        self.time_quantity = ''
        self.timeline = None

    def generateTimeline(self, make_up):
        self.timeline_tile = make_up[0]
        self.data_range = make_up[1]
        self.time_unit = make_up[2]
        self.time_quantity = make_up[3]
        print(make_up)
