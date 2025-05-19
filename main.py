import src.FileReading as fr


def main():
    reader = fr.FileReading("./data/Yuksel", "Gezegenler.txt",
                            "Araclar.txt", "Kisiler.txt");

    reader.readPeople();
    reader.readPlanets();
    reader.readSpaceships();



if (__name__ == "__main__"):
    main()