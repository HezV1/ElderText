from elder_level import Level
from sys import exit

class StartPath(object):
    """class for StartPath Scene"""
    def enter(self):
        print """
You are walking north-east along the path to Riverwood. The white river
gurgles and bubbles as it rolls past you. As you check your surroundings, you
notice a path worn into the grass on your right. The path veers of the road
to the east and and curves around the stone outcropping to the south-east.
Inlaid into the incline of the path are wooden slats. A tree borders the path
on the left and sparse shrubbery can be found on the inside of the curve of
the path.
"""
        while True:
            OPTIONS =['follow path']
            print OPTIONS
            choice = raw_input()
            if choice == OPTIONS[0]:
                break
            else:
                pass

        return "entrance"

class Entrance(object):
    """class for Entrance Scene"""
    def enter(self):
        print "Entrance text"
        return "death"

class Death(object):
    """class for death scene"""
    def enter(self):
        print "You died"

class EmbershardMine(Level):
    """Class for ElderText Level"""

    scenes = {
        "start_path" : StartPath(),
        "entrance" : Entrance(),
        "death" : Death(),
    }

    opening_scene = scenes["start_path"]
    last_scene = scenes["death"]
