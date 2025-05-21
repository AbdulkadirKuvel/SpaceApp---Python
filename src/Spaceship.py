from __future__ import annotations
from typing import List
from src.EnumVars import SpacecraftStatus as state
from src.Time import Time
import fontstyle as fs
# from colorama import Fore as f

class Spacecraft():
    def __init__(
            self,
            name: str,
            planet_dep: str,
            planet_arr: str,
            departure_date: str,
            distance: int
    ):
        self.name = name
        self.depart_str = planet_dep
        self.arrival_str = planet_arr
        self.dep_date = Time(departure_date)
        self.arr_date: Time
        self.distance = distance
        self.depart_obj: "Planet" # type: ignore
        self.arrival_obj: "Planet" # type: ignore
        self.crew: List["Person"] = [] # type: ignore
        self.status = state.IDLE

    def check_crew(self) -> None:
        for person in self.crew:
            if (person.update()):
                self.crew.remove(person)
                return

    def get_crew_size(self) -> int:
        return len(self.crew)

    def any_alive(self) -> bool:
        for person in self.crew:
            if (person.alive):
                return True
        return False

    def eval_arrival(self) -> None:
        days_wait = self.dep_date - self.depart_obj.date
        hours_wait = days_wait * self.depart_obj.date.max_hour
        hours_total = self.distance + hours_wait

        days_total = hours_total // self.arrival_obj.date.max_hour
        self.arr_date = self.arrival_obj.date.copy()
        self.arr_date.forward_days(days_total)

    def update(self) -> int:
        self.check_crew()
        
        if (self.status == state.DESTROYED):
            return 1
        
        elif not (self.any_alive()):
            self.status = state.DESTROYED
            return 1

        elif (self.status == state.DOCKED):
            self.arrival_obj.add_population(self.get_crew_size())
            return 1
        
        elif (self.status == state.IDLE):
            if (self.dep_date == self.depart_obj.date):
                self.status = state.IN_TRANSIT
            else:
                self.depart_obj.add_population(self.get_crew_size())

        else: # IN_TRANSIT
            self.distance -= 1
            if (self.distance <= 0):
                self.status = state.DOCKED
                self.arrival_obj.add_population(self.get_crew_size())
                return 1
            
        return 0
    
    def color(self) -> str:
        if (self.status == state.DOCKED):
            return fs.apply("DOCKED", "green")
        elif (self.status == state.IN_TRANSIT):
            return fs.apply("IN TRANSIT", "yellow")
        elif (self.status == state.IDLE):
            return fs.apply("IDLE", "blue")
        else:
            return fs.apply("DESTROYED", "red")
        
    def __str__(self):
        distance_str = str(self.distance) if self.status != state.DESTROYED else '--'
        arr_str = str(self.arr_date) if self.status != state.DESTROYED else '--'
        text = self.color()
        return f"{self.name:<12} {text:<12}\t  {self.depart_str:<12} {self.arrival_str:<12} {distance_str:<12} {arr_str:<12}"