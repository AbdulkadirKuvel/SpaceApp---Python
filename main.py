# from src.Simulation import Simulation
# import src.utils.FileReading as fr
# import src.utils.FileWriting as fw
import src.visualization as vis
from src.Simulator import Simulator
import fontstyle as fs
from readchar import readkey, key # type: ignore
import os
import sys


def visualizer():
    visualize = vis.Visualization("./data_out/My datas", "Gezegenler.csv",
                            "Araclar.csv", "Kisiler.csv")

    visualize.read_data()
    # visualize.plot_planets()
    visualize.plot_spacecrafts()
    print("Visualization completed.")

def clear_lines(n=1):
    for _ in range(n):
        sys.stdout.write("\033[F")  # Cursor'u yukarı taşı
        sys.stdout.write("\033[K")  # Satırı temizle

def visualization_menu():
    pass

def main():
    simulator = Simulator()
    print()
    print(fs.apply("-- Spacecraft Simulation --", "cyan"))

    ax1 = fs.apply(">>", "yellow")
    ax2 = fs.apply("  ", "yellow")
    ax3 = fs.apply("  ", "yellow")

    line = 1

    while True:
        trash = 3
        
        print(f"{ax1} Simulation")
        print(f"{ax2} Visualization")
        print(f"{ax3} Exit")
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
                simulator.menu()
                trash += 7
            elif line == 2:
                visualization_menu()
            elif line == 3:
                print("Exiting...")
                break
        else:
            pass
        
        if line == 1:
            ax1 = fs.apply(">>", "yellow")
            ax2 = fs.apply("  ", "yellow")
            ax3 = fs.apply("  ", "yellow")
        elif line == 2:
            ax1 = fs.apply("  ", "yellow")
            ax2 = fs.apply(">>", "yellow")
            ax3 = fs.apply("  ", "yellow")
            
        elif line == 3:
            ax1 = fs.apply("  ", "yellow")
            ax2 = fs.apply("  ", "yellow")
            ax3 = fs.apply(">>", "yellow")
            
        clear_lines(trash)

if (__name__ == "__main__"):
    main()
