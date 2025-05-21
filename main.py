import src.FileReading as fr
from src.Simulation import Simulation


def main():
    reader = fr.FileReading("./data/My datas/Old", "Gezegenler.txt",
                            "Araclar.txt", "Kisiler.txt")

    people = reader.readPeople()
    spacecrafts = reader.readSpaceships()
    planets = reader.readPlanets()

    simulation = Simulation(people, spacecrafts, planets)

    simulation.connector()
    simulation.simulate()


if (__name__ == "__main__"):
    main()