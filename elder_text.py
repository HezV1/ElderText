from sys import exit, argv
import importlib
print ("*** loading engine ***")
from elder_engine import Engine
print ("*** loading level ***")
from world import levels
level_code = raw_input('Grab Level Code')
level = importlib.import_module(levels[level_code], 'SubLevel')

options = []

level_a = level.SubLevel()
engine_a = Engine(level_a)
while True:
    level_code = engine_a.play()
    level = importlib.import_module(levels[level_code], 'SubLevel')

    level_a = level.SubLevel()
    engine_a.level = level_a





