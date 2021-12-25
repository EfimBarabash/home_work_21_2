class UnitDied(Exception):
    pass


class Unit:
    got_key = False
    escaped = False

    def __init__(self, hp: int, coords: tuple):
        self.hp = hp
        self.coords = coords

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        return self.escaped

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if not self.is_alive():
            raise UnitDied('Персонаж погиб')

    def set_coordinates(self, x, y):
        self.coords = (x, y)

    def get_coordinates(self):
        return self.coords

    def has_position(self, x, y):
        return self.coords == (x, y)


class Ghost(Unit):

    def __init__(self, hp: int, coords: tuple):
        super().__init__(hp, coords)
        self.name = 'Ghost'


