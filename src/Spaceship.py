from typing import List
from src.Person import Person
from src.Planets.Planet import Planet
from src.EnumVars import SpacecraftStatus as state
from src.Time import Time

class Spacecraft():
    def __init__(
            self,
            name: str,
            planet_dep: str,
            planet_arr: str,
            departure_date: str,
            distance: int
    ):
        self.name = name
        self.depart_str = planet_dep
        self.arrival_str = planet_arr
        self.dep_date = Time(departure_date)
        self.distance = distance
        self.depart_obj: Planet
        self.arrival_obj: Planet
        self.crew: List[Person] = []
        self.status = state.IDLE

    def get_crew_size(self) -> int:
        return len(self.crew)

    def any_alive(self) -> bool:
        for person in self.crew:
            if (person.alive):
                return True
        return False

    def update(self) -> int:
        if (self.status == state.DESTROYED):
            return 1
        
        elif not (self.any_alive()):
            self.status = state.DESTROYED
            return 1

        elif (self.status == state.DOCKED):
            return 1
        
        elif (self.status == state.IDLE):
            if (self.dep_date == self.depart_obj.date):
                self.status = state.IN_TRANSIT

        else:
            if (self.distance <= 0):
                self.status = state.DOCKED
                return 1
            self.distance -= 1
            
        return 0
        
