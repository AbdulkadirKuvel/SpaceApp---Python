import src.FileReading as fr


def main():
    reader = fr.FileReading("./data/Yuksel", "Gezegenler.txt",
                            "Araclar.txt", "Kisiler.txt");

    people = reader.readPeople();
    planets = reader.readPlanets();
    spacecrafts = reader.readSpaceships();




if (__name__ == "__main__"):
    main()