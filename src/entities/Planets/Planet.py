from src.time_system.Time import Time
from src.entities.Spacecraft import Spacecraft

class Planet():
    def __init__(
            self,
            name: str,
            hours_per_day: int,
            date: str
    ):

        self.name = name
        self.date = Time(date, hours_per_day)
        self.population = 0
        # self.curr_spacecrafts: List[Spacecraft] = []

    # def add_spacecraft(self, spacecraft: Spacecraft) -> None:
    #     self.curr_spacecrafts.append(spacecraft)
    #     self.incorrect_population = True

    # def remove_spacecraft(self, spacecraft: Spacecraft) -> None:
    #     self.curr_spacecrafts.remove(spacecraft)
    #     self.incorrect_population = True

    def add_population(self, population: int) -> None:
        self.population += population

    def sub_population(self, population: int) -> None:
        self.population -= population

    def get_population(self) -> int:
        return self.population

    def update(self):
        self.date.forward_hours()
