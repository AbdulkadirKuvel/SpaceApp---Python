class Spacecraft():
    def __init__(
            self,
            name: str,
            planet_dep: str,
            planet_arr: str,
            departure_date: str,
            distance: int
    ):
        self.name = name;
        self.depart_str = planet_dep;
        self.arrival_str = planet_arr;
        self.dep_date = departure_date;
        self.distance = distance;
        self.depart = None;
        self.arrival = None;

    def connect_planet(self):
        pass;

    def update(self):
        pass;

