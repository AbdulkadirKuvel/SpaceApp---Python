import os
import sys
from src.utils.FileReading import FileReading
from src.visualization import Visualization
import fontstyle as fs
from readchar import readkey, key  # type: ignore

def clear_lines(n=1):
    for _ in range(n):
        sys.stdout.write("\033[F")  # Cursor'u yukarı taşı
        sys.stdout.write("\033[K")  # Satırı temizle

class Visualizer():
    def  __init__(self):
        main_path = ".\\data\\Visualization"
        self.people_file = os.path.join(main_path, "Kisiler.csv")
        self.spacecraft_file = os.path.join(main_path, "Araclar.csv")
        self.planets_file = os.path.join(main_path, "Gezegenler.csv")

        self.reader = FileReading(self.people_file,
                                  self.spacecraft_file,
                                  self.planets_file)

        self.visualizer: Visualization = NotImplemented
        self.files_ok = True

    
    def menu(self):
        ax1 = fs.apply("sim >>", "purple")
        ax2 = fs.apply("      ", "purple")
        ax3 = fs.apply("      ", "purple")

        line = 1
        while True:
            self.files_ok = self.reader.check_paths()
            while True:
                trash = 3
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
                        # self.simulate()
                        trash = 0
                    elif line == 2:
                        self.reader.path_changer_menu()
                        clear_lines(15)
                        break
                    elif line == 3:
                        return
                else:
                    pass

                clear_lines(trash)

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