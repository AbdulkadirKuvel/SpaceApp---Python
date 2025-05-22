class Person():
    def __init__(self, name: str, age: int, 
                 left_hours: float, spaceship_name: str):
        self.name = name
        self.age = age
        self.left_hours = left_hours
        self.spaceship_name = spaceship_name
        self.alive = True

    def update(self):
        self.left_hours -= 1
        if self.left_hours <= 0:
            self.alive = False
            return 1
        return 0
