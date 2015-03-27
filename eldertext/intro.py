from elder_level import Level
from sys import exit

class Start(object):
    """Class for Start Scene"""
    def enter(self):
        print """
You come to staring at a wooden floor. You can feel your body jostling, as you
lift your head you realize you are on a cart being pulled by a horse. The
driver of the cart is a nord wearing red leather armor. The cart has two
benches on either side. You sit on the front left position. A blonde nord sits
across from you dressed in blue armor,his hands are bound and as you look
down, you see that yours are as well.

As you glance around in front of you, you see that you are being driven down a
stone road through a cold tundra. There is another cart ahead of you, and in
front of that, another red guard riding on horseback There are trees on both
sides of the road as well as rocky outcroppings, everything has a light
blanket of snow around it.
        """
        raw_input()
        print """
The blonde nord seated next to you looks up at you and says,

  " Hey, you. You're finaly awake. You were trying to cross the border,
    right? Walked right into that imperial ambush, same as us, and that thief
    over there. "

Turning to your right, you see another nord tied at the wrists, in a cheap
brown tunic. "Damn Stormcloaks. Skyrim was fine until you came along." You
notice that there is a 3rd nord seated on the same bench behind you. He is
wearing the same blue armor as the nord seated next to you but more extravagant
with furs on the shoulder. Not only is this one bound at the wrists, but also
has a wrap tied tightly around his mouth.
        """
        raw_input()
        print """
"Empire was nice and lazy. If they hadn't been looking for you, id have stolen
that horse and be halfway
to Hammerfel." The thief looks at you and says,
"You there, you and me, we shouldn't be here it's these stormcloaks the empire
wants."

"Were all brothers and sisters in binds now, thief," said the blonde nord.

The guard driving the cart shouts, "Shut up back

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
    last_scene = [scenes["death"]]
