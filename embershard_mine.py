from elder_level import Level

class StartPath(object):
    """class for StartPath Scene"""
    def enter(self):
        print "StartPath text"
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
    def __init__(self):
        self.maze = Level()

    scenes = {
        "start_path" : StartPath(),
        "entrance" : Entrance(),
        "death" : Death(),
    }

    opening_scene = scenes["start_path"]
    last_scene = scenes["death"]
