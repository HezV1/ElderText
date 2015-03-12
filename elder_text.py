from sys import exit, argv
import importlib
print ("*** loading engine ***")
from elder_engine import Engine
print ("*** loading level ***")
level = raw_input('Grab Level Code')
level_b = importlib.import_module(level, 'SubLevel')

OPTIONS = []

level_a = level_b.SubLevel()
engine_a = Engine(level_a)
engine_a.play()



