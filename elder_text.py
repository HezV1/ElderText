from sys import exit, argv
import importlib
print ("*** loading engine ***")
from elder_engine import Engine
print ("*** loading level ***")
from world import levels
level = raw_input('Grab Level Code')
level_b = importlib.import_module(levels[level], 'SubLevel')

OPTIONS = []

level_a = level_b.SubLevel()
engine_a = Engine(level_a)
engine_a.play()



