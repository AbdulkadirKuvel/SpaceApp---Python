from typing import List
from src.entities.Person import Person
from src.entities.Spacecraft import Spacecraft
from src.entities.Planets.Planet import Planet
from src.EnumVars import SpacecraftStatus as state
import os
from time import sleep

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
        print("Planets:")
        cell_width = 15

        # Başlıklar
        names_row = "\t\t" + "".join(f"-- {p.name.ljust(cell_width - 7)} -- " for p in self.planets)
        date_row  = "Date:\t\t" + "".join(f"{str(p.date).ljust(cell_width)}" for p in self.planets)
        pop_row   = "Population:\t" + "".join(f"{str(p.population).ljust(cell_width)}" for p in self.planets)

        print(names_row)
        print(date_row)
        print(pop_row)

        print("\nSpacecrafts:")
        print(f"{'Name':<12} {'Status':<12} {'Departure':<12} {'Arrival':<12} {'Distance':<12} {'Arrival Date':<12}")
        for spacecraft in self.spacecrafts:
            print(spacecraft)

    def connector(self) -> None:
        for spacecraft in self.spacecrafts:
            for person in self.people:
                if (person.spaceship_name == spacecraft.name):
                    spacecraft.crew.append(person)

            for planet in self.planets:
                if (planet.name == spacecraft.depart_str):
                    spacecraft.depart_obj = planet
                    planet.add_population(spacecraft.get_crew_size())
                elif (planet.name == spacecraft.arrival_str):
                    spacecraft.arrival_obj = planet
            
            spacecraft.eval_arrival()

    def simulate(self):
        self.connector()
                
        itr = 1
        while(1):
            sleep(.020)
            for planet in self.planets:
                planet.update()
                planet.population = 0

            finished = 0

            for spacecraft in self.spacecrafts:
                finished += spacecraft.update()

            self.printer()

            print(f"--> Total Iteration: {itr}")
            itr += 1

            if finished == len(self.spacecrafts):
                print("Simulation End.")
                break