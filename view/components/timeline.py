from Database import Database


class Timeline:
    def __init__(self):
        self.__db = Database.DataBase()
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
        attained = self.attainData(self.data_range)

    def convertTime(self, time):
        time.remove('')
        date = []
        value = ''
        for j in time:
            for i in j:
                if i.isnumeric():
                    value = value + i
                else:
                    date.append(int(value))
                    value = ''
            date.append(int(value))
            value = ''
        return date

    def attainData(self, time):
        time = time.split('-')  # split into sections start date time - end date time
        print(time)
        start = self.convertTime(time[0].split(' '))
        end = self.convertTime(time[1].split(' '))
        print(start)
        print(end)

        return True









