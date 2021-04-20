class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def format_hours(self):
        if len(str(self.hours)) == 1:
            return f'0{self.hours}'
        return self.hours

    def format_minutes(self):
        if len(str(self.minutes)) == 1:
            return f'0{self.minutes}'
        return self.minutes

    def format_seconds(self):
        if len(str(self.seconds)) == 1:
            return f'0{self.seconds}'
        return self.seconds

    def validate_time(self):
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1

        if self.hours > Time.max_hours:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        Time.validate_time(self)

    def get_time(self):
        Time.validate_time(self)
        h = Time.format_hours(self)
        m = Time.format_minutes(self)
        s = Time.format_seconds(self)

        return f'{h}:{m}:{s}'

    def next_second(self):
        self.seconds += 1

        return Time.get_time(self)

# Test code
# time = Time(9, 30, 59)
# print(time.next_second())
#
# time = Time(10, 59, 59)
# print(time.next_second())
#
# time = Time(23, 59, 59)
# print(time.next_second())
