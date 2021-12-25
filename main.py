from controller import GameController

levl_one = '''WWWWWWWWWW
WggGgggggW
WgTTTggDgW
WKggggTggW
WWWWWWWWWW'''

levl_two = '''ggggg
gGggg
ggggD
'''


if __name__ == '__main__':
    gc = GameController()
    gc.load_fiedl(levl_one)
    gc.play()
