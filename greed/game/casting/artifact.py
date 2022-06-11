from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

import random





class Item(Actor):
    def __init__(self):
        super().__init__()
        self._rock_or_gem = ""
        self._message = ""
        


    def set_item_type(self):
        num = random.randint(1,2)
        if num == 1:
            self._rock_or_gem = "rock"
        elif num == 2:
            self._rock_or_gem = "gem"
        pass
    
    def fall(self, max_y):
        x = (self._position.get_x())
        y = (self._position.get_y() + 2) % max_y
        self._position = Point(x, y)

    def get_item_type(self):
        return self._rock_or_gem

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message
