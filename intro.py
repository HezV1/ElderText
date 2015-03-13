from elder_level import Level
from sys import exit

class Start(object):
    """Class for Start Scene"""
    def enter(self):
        print """
You come to staring at a wooden floor. You can feel your body jostling, as you
lift your head you realize you are on a cart being pulled by a horse. The cart
has two benches on either side, the cart fits 2 on the benches. You sit on the
front left position. A nord sits across from you dressed in blue leather s

        """
        return "character_creation"

class CharacterCreation(object):
    """Class for CharacterCreation Scene"""
    def enter(self):
        print "CharacterCreation Text"
        return "death"

class Death(object):
    """Class for Death Scene"""
    def enter(self):
        print "You died"
        exit()

class SubLevel(Level):
    """Class for Intro Level"""

    scenes = {
        "start" : Start(),
        "character_creation" : CharacterCreation(),
        "death" : Death(),
    }

    opening_scene = scenes["start"]
    last_scene = scenes["death"]
