from game.casting.actor import Actor
from game.shared.point import Point

import random

class Item(Actor):

    """construct an item"""
    def __init__(self):
        super().__init__()
        self._rock_or_gem = ""
        self._message = ""
        


    def set_item_type(self):

        """Generate a ramdom value display a rock or a gem"""
        num = random.randint(1,3)
        if num == 1:
            self._rock_or_gem = "rock"
        elif num == 2:
            self._rock_or_gem = "gem"
        elif num == 3:
            self._rock_or_gem = "asteroid"
        pass
    
    def fall(self, max_y):

        """method to give move the elements in axis Y and falldown"""
        x = (self._position.get_x())
        y = (self._position.get_y() + 2) % max_y
        self._position = Point(x, y)

    def get_item_type(self):

        """method to return the ramdon element generated"""
        return self._rock_or_gem

    def get_message(self):

        """Method to return a message if the player gets a rock or gem"""
        return self._message

    def set_message(self, message):
        """Method to set the message to show to the palyer if it's a gem or rock"""
        self._message = message
