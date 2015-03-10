from elder_level import Level

class StartPath(object):
    """class for StartPath Scene"""
    def enter(self):
        print "While walking along the road to Riverwood, you notice an area"
        print "Between two of the trees you can see a path worn away in the"
        print "dirt. Upon the slope of the path that leads north, you can see"
        print "a few wooden slats embeded in the ground. The path curves to"
        print "the right behind some shrubs."
        OPTIONS =['go']
        print OPTIONS
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
