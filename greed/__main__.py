from game.casting.actor import Actor
from game.casting.artifact import Item
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():    
    """Create the objet cast """ 
    cast = Cast()
    
    create_banner(cast)    
    create_robot(cast)   
    initialize_services(cast)

""" Create the banner to display in the game"""
def create_banner(cast):
    banner = Actor()
    banner.set_text("Score: ")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    banner2 = Actor()
    banner2.set_text("Go!")
    banner2.set_font_size(FONT_SIZE)
    banner2.set_color(WHITE)
    banner2.set_position(Point(700, 0))
    cast.add_actor("banners", banner2)

"""Create the robot """
def create_robot(cast):
    x = int(MAX_X / 2)
    y = int(MAX_Y - 619)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

""" Initialize services that game use and start """
def initialize_services(cast):
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()