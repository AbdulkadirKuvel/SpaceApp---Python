class FileReading():
    def __init__(self, path: str,
                 planets_file_name: str,
                 spaceship_file_name: str,
                 people_file_name: str):
        self.path = path;
        self.planet_path = planets_file_name;
        self.spaceship_path = spaceship_file_name;
        self.people_path = people_file_name;

    def readPlanets(self):
        with open(self.path + "/" + self.planet_path, encoding="utf-8") as file:
            line = file.readline();
            print(line);

    def readSpaceships(self):
        with open(self.path + "/" + self.spaceship_path, encoding="utf-8") as file:
            line = file.readline();
            print(line);
            

    def readPeople(self):
        with open(self.path + "/" + self.people_path, encoding="utf-8") as file:
            line = file.readline();
            print(line);
            