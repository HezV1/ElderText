from elder_level import level
from sys import exit

class Start(object):
    """class for Start Scene"""
    def enter(self):
        print "Start Text"
        return "character_creation"

class CharacterCreation(object):
    """class for CharacterCreation Scene"""
    def enter(self):
        print "CharacterCreation Text"
        return "death"

class Death(object):
    """class for Death Scene"""
    def enter(self):
        print "You died"

class Intro(Level):
    """Class for Intro Level"""

    scenes = {
        "start" : Start(),
        "character_creation" : CharacterCreation(),
        "death" : Death(),
    }

    opening_scene = scenes["start"]
    last_scene = scenes["death"]
