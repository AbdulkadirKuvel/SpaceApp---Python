# import numpy as np # type: ignore
import src.Planets.Planet as pl
import src.Spaceship as ss
import src.Person as p

class FileReading():
    def __init__(self, main_folder_path: str,
                 planets_file_name: str,
                 spaceship_file_name: str,
                 people_file_name: str):
        self.path = main_folder_path;
        self.planet_path = planets_file_name;
        self.spaceship_path = spaceship_file_name;
        self.people_path = people_file_name;
        
        self.spacecrafts = list();
        self.planets = list(); # TODO
        self.people = list();

    def readPlanets(self):
        with open(self.path + "/" + self.planet_path, encoding="utf-8") as file:
            while(1):
                line = file.readline();
                if (line == ""):
                    break;
                line = line.rstrip();
                parts = line.split("#");
                name = parts[0];
                kind = parts[1]; # TODO
                hours_of_a_day = int(parts[2]);
                date = parts[3];
                planet = pl.Planet(name, hours_of_a_day, date);
                self.planets.append(planet);
        

    def readSpaceships(self):
        with open(self.path + "/" + self.spaceship_path, encoding="utf-8") as file:
            while (1):
                line = file.readline();
                if (line == ""):
                    break;
                line = line.rstrip();
                parts = line.split("#");
                name = parts[0];
                departure = parts[1];
                arrival = parts[2];
                departure_date = parts[3];
                distance = int(parts[4]);
                spacecraft = ss.Spacecraft(name, departure,
                                    arrival, departure_date,
                                    distance);
                self.spacecrafts.append(spacecraft);
        return self.spacecrafts;

    def readPeople(self):
        with open(self.path + "/" + self.people_path, encoding="utf-8") as file:
            while(1):
                line = file.readline();
                if (line == ""):
                    break;
                line = line.rstrip();
                parts = line.split("#");
                name = parts[0];
                age = int(parts[1]);
                left_hours = float(parts[2]);
                spacecraft = parts[3];
                person = p.Person(name, age, left_hours, spacecraft)
                self.people.append(person);
        return self.people;