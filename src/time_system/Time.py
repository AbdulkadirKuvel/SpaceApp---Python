from datetime import datetime, timedelta, date

class Time():
    def __init__(self, date_str: str | date, max_hours = 0):
        if isinstance(date_str, str):
            self.date = self.str_to_date(date_str)
        else: # date
            self.date = date_str
        self.max_hour = max_hours
        self.hour = 0

    def str_to_date(self, date: str) -> date:
        return datetime.strptime(date, "%d.%m.%Y").date()
    
    def forward_hours(self, hours = 1):
        if (self.max_hour == 0):
            return
        self.hour += hours
        if (self.hour >= self.max_hour):
            days = self.hour // self.max_hour
            self.hour %= self.max_hour
            self.hour = 0
            self.forward_days(days)
    
    def forward_days(self, days = 1):
        self.date += timedelta(days)

    def copy(self) -> "Time":
        new_time = Time(self.date.strftime("%d.%m.%Y"), self.max_hour)
        new_time.hour = self.hour
        return new_time

    def __sub__(self, value: object) -> int:
        if not isinstance(value, Time):
            return NotImplemented
        return (self.date - value.date).days

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Time):
            return NotImplemented
        return self.date == value.date

    def __str__(self):
        return self.date.strftime("%d.%m.%Y")
    
    def __format__(self, _format: str):
        return format(str(self), _format)