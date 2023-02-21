class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.seconds == 0:
            self.seconds = "00"
        elif self.seconds <= 9:
            self.seconds = f"0{self.seconds}"

        if self.minutes == 0:
            self.minutes = "00"
        elif self.minutes <= 9:
            self.minutes = f"0{self.minutes}"

        if self.hours == 0:
            self.hours = "00"
        elif self.hours <= 9:
            self.hours = f"0{self.hours}"

        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        result = self.get_time()
        return result


time = Time(9, 30, 59)
print(time.next_second())






