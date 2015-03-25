class Engine(object):
    """Game Engine for ElderText"""
    def __init__(self, level):
        self.level = level

    def play(self):
        current_scene = self.level.opening_scene
        last_scene = self.level.last_scene

        while current_scene not in self.level.last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.level.next_scene(next_scene_name)

        return current_scene.enter()
