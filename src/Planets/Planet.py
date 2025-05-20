class Planet():
    def __init__(
            self,
            name: str,
            hours_per_day: int,
            date: str
    ):
        
        self.name = name;
        self.day_hours = hours_per_day;
        self.date = date;

    def update(self):
        pass