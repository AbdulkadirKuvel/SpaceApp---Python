from typing import List
from src.Person import Person
from src.Spaceship import Spacecraft
from src.Planets.Planet import Planet
import os

class Simulation():
    def __init__(
            self, 
            people: List[Person],
            spacecrafts: List[Spacecraft],
            planets: List[Planet]
    ):
        self.people = people
        self.spacecrafts = spacecrafts
        self.planets = planets

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def printer(self) -> None:
        self.clear()
        print("Gezegenler:")
        

    def connector(self) -> None:
        for spacecraft in self.spacecrafts:
            for person in self.people:
                if (person.spaceship_name == spacecraft.name):
                    spacecraft.crew.append(person)

            for planet in self.planets:
                if (planet.name == spacecraft.depart_str):
                    spacecraft.depart_obj = planet
                elif (planet.name == spacecraft.arrival_str):
                    spacecraft.arrival_obj = planet

    def simulate(self):
        itr = 1
        while(1):
            self.printer()
            
            for planet in self.planets:
                planet.update()
            
            for spacecraft in self.spacecrafts:
                spacecraft.update()
