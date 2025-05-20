from datetime import datetime, timedelta, date

class Time():
    def __init__(self, date: str, max_hours = 0):
        self.date = self.str_to_date(date)
        self.max_hour = max_hours
        self.hour = 0

    def str_to_date(self, date: str) -> date:
        return datetime.strptime(date, "%d.%m.%Y").date()
    
    def forward_hours(self, hours = 1):
        self.hour += hours
        if (self.hour >= self.max_hour):
            days = self.hour // self.max_hour
            self.hour %= self.max_hour
            self.forward_days(days)
    
    def forward_days(self, days = 1):
        self.date += timedelta(days)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Time):
            return NotImplemented
        return self.date == value.date

    def __str__(self):
        return self.date.strftime("%d.%m.%Y")
    