from game.casting.actor import Actor
import random

class Item(Actor):
    def __init(self):
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

    def get_item_type(self):
        return self._rock_or_gem

    def get_message(self):
        if self._rock_or_gem == "rock":
            self._message = "Oops! That was a rock!"
        elif self._rock_or_gem == "gem":
            self._message = "Nice!"
        pass
