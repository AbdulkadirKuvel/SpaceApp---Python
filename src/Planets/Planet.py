from src.Time import Time
from typing import List
from src.Spaceship import Spacecraft

class Planet():
    def __init__(
            self,
            name: str,
            hours_per_day: int,
            date: str
    ):
        
        self.name = name;
        self.date = Time(date, hours_per_day);
        self.population = 0
        self.incorrect_population = True
        self.curr_spacecrafts: List[Spacecraft] = []

    def add_spacecraft(self, spacecraft: Spacecraft) -> None:
        self.curr_spacecrafts.append(spacecraft)
        self.incorrect_population = True

    def remove_spacecraft(self, spacecraft: Spacecraft) -> None:
        self.curr_spacecrafts.remove(spacecraft)
        self.incorrect_population = True

    def get_population(self) -> int:
        if (self.incorrect_population):
            self.population = sum([spacecraft.get_crew_size() for spacecraft in self.curr_spacecrafts])
            self.incorrect_population = False
        return self.population

    def update(self):
        self.date.forward_hours()