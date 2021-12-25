from hero import Unit, Ghost


class Terrain:

    def __init__(self, terrain: str = 'Terrain', walkable: bool = True):
        self.terrain = terrain
        self.walkable = walkable

    def step_on(self, unit: Unit):
        pass

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain


class Door(Terrain):

    def __init__(self):
        super().__init__(terrain='Door', walkable=True)

    def step_on(self, unit: Unit):
        if unit.has_key():
            unit.escaped = True


class Key(Terrain):

    def __init__(self):
        super().__init__(terrain='Key', walkable=True)

    def step_on(self, unit: Unit):
        unit.set_key()


class Trap(Terrain):

    def __init__(self):
        super().__init__(terrain='Trap', walkable=True)
        self.damage = 1

    def step_on(self, unit: Unit):
        unit.get_damage(self.damage)


class Wall(Terrain):

    def __init__(self):
        super().__init__(terrain='Wall', walkable=False)


class Grass(Terrain):

    def __init__(self):
        super().__init__(terrain='Grass', walkable=True)


if __name__ == '__main__':
    hero = Ghost(10, (1, 1))
    trap = Trap()
    key = Key()
    door = Door()
    grass = Grass()

    trap.step_on(hero)
    grass.step_on(hero)
    door.step_on(hero)
    key.step_on(hero)
    door.step_on(hero)

