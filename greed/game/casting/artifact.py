from game.casting.actor import Actor
import random

class Item(Actor):
    def __init(self):
        super().__init__()
        self._rock_or_gem = ""

    def set_item_type(self):
        num = random.randint(1,2)
        if num == 1:
            self._rock_or_gem = "rock"
        elif num == 2:
            self._rock_or_gem = "gem"
        pass

    def get_item_type(self):
        return self._rock_or_gem
