import fontstyle as fs # type: ignore
from readchar import readkey, key  # type: ignore
from src.utils.FileReading import FileReading
from src.Simulation import Simulation
import os
import sys
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_lines(n = 1):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

class Simulator():
    def __init__(self):
        main_path = ".\\data_in\\My datas"
        self.people_file = os.path.join(main_path, "Kisiler.txt")
        self.spacecraft_file = os.path.join(main_path, "Araclar.txt")
        self.planets_file = os.path.join(main_path, "Gezegenler.txt")

        self.reader = FileReading(self.people_file,
                                  self.spacecraft_file,
                                  self.planets_file)
        self.simulator: Simulation = NotImplemented
        self.OK = True

    def simulate(self):
        try:
            self.read_files()
            self.simulator.simulate()
            clear()
        except FileNotFoundError:
            print(fs.apply("Missing File: Please check the files", "red"))
            readkey()
            clear_lines(1)
            

    def read_files(self):
        if (not self.OK):
            raise FileNotFoundError
        else:
            people = self.reader.readPeople()
            spacecrafts = self.reader.readSpaceships()
            planets = self.reader.readPlanets()
            self.simulator = Simulation(people, spacecrafts, planets)

    def menu(self):
        while True:
            print(fs.apply("startup: Searching files in default path", "yellow"))

            print(f"Searching {self.people_file} \t", end="")
            if (self.reader.control_people()):
                print(fs.apply("OK", "green"))
            else:
                print(fs.apply("FAILED", "red"))
                self.OK = False

            print(f"Searching {self.spacecraft_file} \t", end="")
            if (self.reader.control_spacecrafts()):
                print(fs.apply("OK", "green"))
            else:
                print(fs.apply("FAILED", "red"))
                self.OK = False

            print(f"Searching {self.planets_file} \t", end="")
            if (self.reader.control_planets()):
                print(fs.apply("OK", "green"))
            else:
                print(fs.apply("FAILED", "red"))
                self.OK = False

            ax1 = fs.apply("sim >>", "purple")
            ax2 = fs.apply("      ", "purple")
            ax3 = fs.apply("      ", "purple")

            line = 1

            while True:
                print(f"{ax1} Start Simulation")
                print(f"{ax2} Change paths")
                print(f"{ax3} Back")
                _key = readkey()
                if _key == key.UP:
                    line -= 1
                    if line < 1:
                        line = 3
                elif _key == key.DOWN:
                    line += 1
                    if line > 3:
                        line = 1
                elif _key == key.ENTER:
                    if line == 1:
                        self.simulate()
                    elif line == 2:
                        self.reader.path_changer_menu()
                        clear_lines(8)
                        break
                    elif line == 3:
                        clear_lines(7)
                        return
                else:
                    pass

                if line == 1:
                    ax1 = fs.apply("sim >>", "purple")
                    ax2 = fs.apply("      ", "")
                    ax3 = fs.apply("      ", "")
                    
                elif line == 2:
                    ax1 = fs.apply("      ", "")
                    ax2 = fs.apply("sim >>", "purple")
                    ax3 = fs.apply("      ", "")

                elif line == 3:
                    ax1 = fs.apply("      ", "")
                    ax2 = fs.apply("      ", "")
                    ax3 = fs.apply("sim >>", "purple")

                clear_lines(3)