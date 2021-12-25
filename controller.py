from hero import Ghost
import terrain
from field import Cell, Field


class GameController:
    def __init__(self):
        self.mapping = {
            'Wall': '🔲',
            'Grass': '🔳',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }
        self.game_on = True
        self.hero = None
        self.field = None

    def load_fiedl(self, levlstring):
        #Метод для загрузки карты
        hero = None
        key = None
        door = None
        field = []
        arr = [[*row] for row in levlstring.split()]
        for i in range(len(arr)):
            row = []
            for j in range(len(arr[i])):
                if arr[i][j] == 'W':
                    row.append(Cell(terrain.Wall()))
                elif arr[i][j] == 'g':
                    row.append(Cell(terrain.Grass()))
                elif arr[i][j] == 'T':
                    row.append(Cell(terrain.Trap()))
                elif arr[i][j] == 'D':
                    door = Cell(terrain.Door())
                    row.append(door)
                elif arr[i][j] == 'K':
                    key = Cell(terrain.Key())
                    row.append(key)
                elif arr[i][j] == 'G':
                    hero = Ghost(1, (j, i))
                    row.append(Cell(hero))
                else:
                    raise ValueError('Некорректное описание карты')
            field.append(row)
        if hero is None:
            raise ValueError('Отсутсвует герой!')
        if door is None:
            raise ValueError('Отсутвует дверь')
        if key is None:
            hero.set_key()
        self.hero = hero
        self.field = Field(field, hero)

    def make_field(self):
        for row in self.field.get_field():
            for elem in row:
                if isinstance(elem.get_obj(), terrain.Terrain):
                    print(self.mapping.get(elem.get_obj().terrain), sep=' ', end='')
                elif isinstance(elem.get_obj(), Ghost):
                    print(self.mapping.get(elem.get_obj().name), sep=' ', end='')
            print()

    def play(self):
        while self.game_on:
            self.make_field()
            command = input('Введите команду :')
            if command == 'stop' or command == 'exit':
                self.game_on = False
            elif command == 'w':
                self.field.move_unit_up()
            elif command == 's':
                self.field.move_unit_down()
            elif command == 'a':
                self.field.move_unit_left()
            elif command == 'd':
               self.field.move_unit_right()
            else:
                print(f'Не такой команды "{command}" \nДоступные команды:\nw-вверх\ns-вниз\na-влево\nd-вправо\nexit, stop-выйти из игры')
            if self.hero.has_escaped():
                print('Поздравляем уровень пройден!')
                self.game_on = False
