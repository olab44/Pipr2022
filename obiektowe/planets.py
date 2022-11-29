from math import sqrt


class Planet:
    def __init__(self, name, moon_amount, location=0):
        if not name:
            raise ValueError('name cannot be empty')
        moon_amount = int(moon_amount)
        if moon_amount < 0:
            raise ValueError('amount cannot be negative')
        X, Y, Z = location
        if len(location) < 3:
            raise ValueError('expected three variables')
        self._name = name
        self._moon_amount = moon_amount
        self._location = location

    def name(self):
        return self._name

    def moon_amount(self):
        return self._moon_amount

    def location(self):
        return self._location

    def set_name(self, new_name):
        if not new_name:
            raise ValueError('name cannot be empty')
        self._name = new_name

    def set_moon_amount(self, new_moons):
        new_moons = int(new_moons)
        if new_moons < 0:
            raise ValueError('moon amount cannot be negative')
        self._moon_amount = new_moons

    def set_location(self, x, y, z):
        new_location = (x, y, z)
        if len(new_location) < 3:
            raise TypeError('expected three values')
        if x < 0 or y < 0 or z < 0:
            raise ValueError('locaiton cannot be negative')
        self._location = new_location

    def info(self):
        return f'{self._name} has {self._moon_amount} moons, his location is {self._location}'

    def __str__(self):
        return self.info()


def distance(mercury, venus):
    mercury = Planet('mercury', 0, (2, 5, 9))
    venus = Planet('venus', 5, (2, 1, 6))
    distance_x = int(abs(mercury._location[0] - venus._location[0]))
    distance_y = int(abs(mercury._location[1] - venus._location[1]))
    distance_z = int(abs(mercury._location[2] - venus._location[2]))
    distance = sqrt((distance_x) ** 2 + (distance_y) ** 2 + (distance_z) ** 2)
    return distance
