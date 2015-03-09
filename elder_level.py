class Level(object):
    """Class for ElderText Level"""

    scenes = {}

    def next_scene(self, name):
        return self.scenes[name]
