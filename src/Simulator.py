import fontstyle as fs # type: ignore
from readchar import readkey, key  # type: ignore
from src.utils.FileReading import FileReading
from src.Simulation import Simulation
import os
import sys

default_path = os.path.join(os.path.dirname(__file__), "..\\data_in\\My datas")
default_people_file = os.path.join(default_path, "Kisiler.txt")
default_spacecraft_file = os.path.join(default_path, "Araclar.txt")
default_planets_file = os.path.join(default_path, "Gezsegenler.txt")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_lines(n = 1):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

class Simulator():
    def __init__(self):
        self.reader = FileReading(default_people_file,
                                  default_spacecraft_file, 
                                  default_planets_file)
        self.simulator : Simulation = NotImplemented
        self.OK = True

    def path_changer_menu(self):
        pass

    def path_changer(self):
        pass

    def simulate(self):
        try:
            self.read_files()
            self.simulator.simulate()
        except FileNotFoundError:
            input(fs.apply("Please check the files", "red"))
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
        print(fs.apply("startup: Searching files in default path", "yellow"))

        print(f"Searching {default_people_file} \t", end="")
        if (self.reader.control_people()):
            print(fs.apply("OK", "green"))
        else:
            print(fs.apply("FAILED", "red"))
            self.OK = False

        print(f"Searching {default_spacecraft_file} \t", end="")
        if (self.reader.control_spacecrafts()):
            print(fs.apply("OK", "green"))
        else:
            print(fs.apply("FAILED", "red"))
            self.OK = False

        print(f"Searching {default_planets_file} \t", end="")
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
                    clear()
                elif line == 2:
                    self.path_changer_menu()
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