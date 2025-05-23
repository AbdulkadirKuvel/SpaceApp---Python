# import numpy as np # type: ignore
from src.entities.Planets.Planet import Planet
from src.entities.Spacecraft import Spacecraft
from src.entities.Person import Person
import fontstyle as fs # type: ignore
from readchar import readkey, key  # type: ignore
from typing import List
import sys
import os

def clear_lines(n = 1):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

class FileReading():
    def __init__(self, people_file_name: str,
                 spaceship_file_name: str,
                 planets_file_name: str):
        self.people_path = people_file_name
        self.spacecraft_path = spaceship_file_name
        self.planet_path = planets_file_name

        self.spacecrafts: List[Spacecraft] = []
        self.planets: List[Planet] = [] # TODO
        self.people: List[Person] = []


    def path_changer_menu(self):
        ax1 = fs.apply("path >>", "green")
        ax2 = fs.apply("       ", "green")
        ax3 = fs.apply("       ", "green")
        ax4 = fs.apply("       ", "green")

        line = 1

        print("Current paths:")
        print(f"People path: {self.people_path}")
        print(f"Spacecraft path: {self.spacecraft_path}")
        print(f"Planet path: {self.planet_path}")

        while True:
            trash = 4
            print(f"{ax1} Change People path")
            print(f"{ax2} Change Spacecraft path")
            print(f"{ax3} Change Planet path")
            print(f"{ax4} Back")
            _key = readkey()
            if _key == key.UP:
                line -= 1
                if line < 1:
                    line = 4
            elif _key == key.DOWN:
                line += 1
                if line > 4:
                    line = 1
            elif _key == key.ENTER:
                if line == 1:
                    self.people_path_changer()
                elif line == 2:
                    self.spacecraft_path_changer()
                elif line == 3:
                    self.planet_path_changer()
                elif line == 4:
                    return
                trash += 2
            else:
                pass
            
            clear_lines(trash)

            if line == 1:
                ax1 = fs.apply("path >>", "green")
                ax2 = fs.apply("       ", "")
                ax3 = fs.apply("       ", "")
                ax4 = fs.apply("       ", "")
                
            elif line == 2:
                ax1 = fs.apply("       ", "")
                ax2 = fs.apply("path >>", "green")
                ax3 = fs.apply("       ", "")
                ax4 = fs.apply("       ", "")

            elif line == 3:
                ax1 = fs.apply("       ", "")
                ax2 = fs.apply("       ", "")
                ax3 = fs.apply("path >>", "green")
                ax4 = fs.apply("       ", "")

            elif line == 4:
                ax1 = fs.apply("       ", "")
                ax2 = fs.apply("       ", "")
                ax3 = fs.apply("       ", "")
                ax4 = fs.apply("path >>", "green")

    def people_path_changer(self):
        self.people_path = input(fs.apply("New path for people file: ", "yellow"))
        print("New path:", self.people_path)
        readkey()

    def spacecraft_path_changer(self):
        self.spacecraft_path = input(fs.apply("New path for spacecraft file: ", "yellow"))
        print("New path:", self.spacecraft_path)
        readkey()

    def planet_path_changer(self):
        self.planets_path = input(fs.apply("New path for planet file: ", "yellow"))
        print("New path:", self.planets_path)
        readkey()

    def check_paths(self):
        print(fs.apply("startup: Searching files in default path", "yellow"))
        
        Ok = True
        print(f"Searching {self.people_path} \t", end="")
        if (self.control_people()):
            print(fs.apply("OK", "green"))
        else:
            print(fs.apply("FAILED", "red"))
            Ok = False

        print(f"Searching {self.spacecraft_path} \t", end="")
        if (self.control_spacecrafts()):
            print(fs.apply("OK", "green"))
        else:
            print(fs.apply("FAILED", "red"))
            Ok = False

        print(f"Searching {self.planet_path} \t", end="")
        if (self.control_planets()):
            print(fs.apply("OK", "green"))
        else:
            print(fs.apply("FAILED", "red"))
            Ok = False
        return Ok

    def control_people(self) -> bool:
        if os.path.exists(self.people_path):
            return True
        else:
            return False

    def control_spacecrafts(self) -> bool:
        if os.path.exists(self.spacecraft_path):
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
        with open(self.spacecraft_path, encoding="utf-8") as file:
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