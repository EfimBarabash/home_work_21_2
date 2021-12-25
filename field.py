import terrain
from hero import Unit


class Cell:

    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj

    def __repr__(self):
        if isinstance(self.obj, terrain.Terrain):
            return self.obj.terrain[0]
        else:
            return self.obj.name[0]


class Field:

    def __init__(self, field: list, unit: Unit):
        self.field = field
        self.unit = unit
        self.cell_under_unit = terrain.Grass()
        self.cols = len(self.field[0])
        self.rows = len(self.field)

    def get_cell(self, x, y):
        if x >= self.cols or x < 0:
            return None
        if y >= self.rows or y < 0:
            return None
        return self.field[y][x]

    def _move(self, x, y):
        current_cell = self.cell_under_unit
        self.get_cell(*self.unit.get_coordinates()).set_obj(current_cell)
        self.cell_under_unit = self.get_cell(x, y).get_obj()
        self.cell_under_unit.step_on(self.unit)
        self.unit.set_coordinates(x, y)
        self.get_cell(x, y).set_obj(self.unit)

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        cell = self.get_cell(x, y - 1)
        if cell is not None and cell.get_obj().is_walkable():
            self._move(x, y - 1)

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        cell = self.get_cell(x, y + 1)
        if cell is not None and cell.get_obj().is_walkable():
            self._move(x, y + 1)

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        cell = self.get_cell(x + 1, y)
        if cell is not None and cell.get_obj().is_walkable():
            self._move(x + 1, y)

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        cell = self.get_cell(x - 1, y)
        if cell is not None and cell.get_obj().is_walkable():
            self._move(x - 1, y)

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows
