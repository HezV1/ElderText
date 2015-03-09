from elder_level import Level

class StartPath(object):
    """class for StartPath Scene"""
    def enter(self):
        print "While walking along the road to Riverwood, you notice an area"
        print "Between two of the trees "
        engine_a.options =['go']
        print engine_a.options
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
