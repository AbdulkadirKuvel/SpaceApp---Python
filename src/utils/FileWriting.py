from typing import List
from src.entities.Planets.Planet import Planet
from src.entities.Spacecraft import Spacecraft
from src.entities.Person import Person

class FileWriting:
    def __init__(self, 
                 main_folder_path : str,
                 planets_file_name : str,
                 spaceship_file_name : str,
                 people_file_name : str,
                 csv: bool = True):
        self.path = main_folder_path
        self.planets_file_name = self.path + "\\" + planets_file_name
        self.spaceship_file_name = self.path + "\\" + spaceship_file_name
        self.people_file_name = self.path + "\\" + people_file_name
        if (csv):
            self.sep = ","
        else:
            self.sep = "#"

    def writePlanets(self, planets: List[Planet]) -> None:
        with open(self.planets_file_name, "w", encoding="utf-8") as file:
            if self.sep == ",":
                file.write("Name,Population,Date\n")
            for planet in planets:
                file.write(f"{planet.name}{self.sep}{planet.population}{self.sep}{str(planet.date)}\n")

    def writeSpaceships(self, spacecrafts: List[Spacecraft]) -> None:
        with open(self.spaceship_file_name, "w", encoding="utf-8") as file:
            if self.sep == ",":
                file.write("Name,Departure,Arrival,Departure Date,Status\n")
            for spacecraft in spacecrafts:
                file.write(f"{spacecraft.name}{self.sep}{spacecraft.depart_str}{self.sep}{spacecraft.arrival_str}{self.sep}{str(spacecraft.dep_date)}{self.sep}{spacecraft.status.name}\n")

    def writePeople(self, people: List[Person]) -> None:
        with open(self.people_file_name, "w", encoding="utf-8") as file:
            if self.sep == ",":
                file.write("Name,Spaceship,Alive\n")
            for person in people:
                file.write(f"{person.name}{self.sep}{person.spaceship_name}{self.sep}{str(person.alive)}\n")