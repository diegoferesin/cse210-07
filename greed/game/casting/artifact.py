from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

import random

CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40



class Item(Actor):
    def __init__(self):
        super().__init__()
        self._rock_or_gem = ""
        self._message = ""
        
    def generate_random_item():
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Item()
        artifact.set_item_type()
        if artifact.get_item_type() == "rock":
            artifact.set_text("o")
        elif artifact.get_item_type() == "gem":
            artifact.set_text("*")
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)

    def set_item_type(self):
        num = random.randint(1,2)
        if num == 1:
            self._rock_or_gem = "rock"
        elif num == 2:
            self._rock_or_gem = "gem"
        pass

    def get_item_type(self):
        return self._rock_or_gem

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message
