# import numpy as np # type: ignore
from src.entities.Planets.Planet import Planet
from src.entities.Spacecraft import Spacecraft
from src.entities.Person import Person
from typing import List
import os

class FileReading():
    def __init__(self, people_file_name: str,
                 spaceship_file_name: str,
                 planets_file_name: str):
        self.people_path = people_file_name
        self.spaceship_path = spaceship_file_name
        self.planet_path = planets_file_name

        self.spacecrafts: List[Spacecraft] = []
        self.planets: List[Planet] = [] # TODO
        self.people: List[Person] = []

    def control_people(self) -> bool:
        if os.path.exists(self.people_path):
            return True
        else:
            return False

    def control_spacecrafts(self) -> bool:
        if os.path.exists(self.spaceship_path):
            return True
        else:
            return False

    def control_planets(self) -> bool:
        if os.path.exists(self.planet_path):
            return True
        else:
            return False


    def readPlanets(self):
        try:
            with open(self.planet_path, encoding="utf-8") as file:
                for line in file:
                    line = line.rstrip()
                    parts = line.split("#")
                    name = parts[0]
                    kind = parts[1] # TODO
                    hours_of_a_day = int(parts[2])
                    date = parts[3]
                    planet = Planet(name, hours_of_a_day, date)
                    self.planets.append(planet)
        except Exception as e:
            print(f"Error reading planets file: {e}")
        return self.planets

    # def readSpaceships(self):
    #     with open(self.path + "/" + self.spaceship_path, encoding="utf-8") as file:
    #         for line in file:
    #     return self.planets

    def readSpaceships(self):
        with open(self.spaceship_path, encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()
                parts = line.split("#")
                name = parts[0]
                departure = parts[1]
                arrival = parts[2]
                departure_date = parts[3]
                distance = int(parts[4])
                spacecraft = Spacecraft(name, departure,
                                    arrival, departure_date,
                                    distance)
                self.spacecrafts.append(spacecraft)
        return self.spacecrafts

    def readPeople(self):
        with open(self.people_path, encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()
                parts = line.split("#")
                name = parts[0]
                age = int(parts[1])
                left_hours = float(parts[2])
                spacecraft = parts[3]
                person = Person(name, age, left_hours, spacecraft)
                self.people.append(person)
        return self.people