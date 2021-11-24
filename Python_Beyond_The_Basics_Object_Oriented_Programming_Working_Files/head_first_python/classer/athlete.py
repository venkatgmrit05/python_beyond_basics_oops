class Athlete(object):
    def __init__(self,
                 a_name,
                 a_dob=None,
                 a_times=[]):

        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def how_big(self):
        size = len(self.thing)
        return size

    def get_coach_data(self,filename):
        try:
            with open(filename,'r') as f:
                data = f.readline()
            line_data = data.strip().split(',')
            if not self.name:
                self.name = line_data[0]
            self.dob = line_data[1]
            self.times = [float(self.sanitize_item(item)) for item in line_data[2:]]


        except IOError as ioerr:
            print('File error: ' + str(ioerr))
            return None

    def sanitize_item(self,item):
        try:
            sanitized_item_tokens = []
            for i in item:
                if i.isalnum():
                    sanitized_item_tokens.append(i)
                else:
                    sanitized_item_tokens.append('.')
            sanitized_item = ''.join(sanitized_item_tokens)
            return sanitized_item

        except Exception as e:
            print("error >> {}".format(e))

    @classmethod
    def sanitize(cls,item):
        try:
            sanitized_item_tokens = []
            for i in item:
                if i.isalnum():
                    sanitized_item_tokens.append(i)
                else:
                    sanitized_item_tokens.append('.')
            sanitized_item = ''.join(sanitized_item_tokens)
            return sanitized_item

        except Exception as e:
            print("error >> {}".format(e))

    def top3(self):

        athlete_times = self.times
        sorted_times = sorted(athlete_times)
        return sorted_times[:3]

    def add_time(self,
                 lap_time):
        # self.times.append(float(self.sanitize_item(lap_time)))
        # self.times.append(float(Athlete.sanitize(lap_time)))
        self.times.append(float(sanitize(lap_time)))

    def add_times(self,
                  lap_time_list):
        for laptime in lap_time_list:
            self.add_time(laptime)


def sanitize(item):
    try:
        sanitized_item_tokens = []
        for i in item:
            if i.isalnum():
                sanitized_item_tokens.append(i)
            else:
                sanitized_item_tokens.append('.')
        sanitized_item = ''.join(sanitized_item_tokens)
        return sanitized_item

    except Exception as e:
        print("error >> {}".format(e))


file = r"james2.txt"
james = Athlete(0)
james.get_coach_data(file)
print(james.name)
print(james.times)
print(james.top3())

james.add_time('1.5')
print(james.times)

james.add_times(['1.5','2.8','1.4'])
print(james.times)
print(james.top3())


vera = Athlete('vera vi')
print(vera.times)
vera.add_time('1.31')
print(vera.times)
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())