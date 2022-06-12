import asyncio

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.points = 0
        self.timer = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()
        print("Great job! You finished with a score of: " + str(self.points))

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        async def actor_generation(cast, artifacts):
            await asyncio.sleep(1)
            cast.add_actor("artifacts", cast.generate_random_item())

        banner = cast.get_first_actor("banners")
        second_banner = cast.get_actors("banners")[-1]
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("Score: " + str(self.points))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            artifact.fall(max_y)
            artifact.move_next(max_x, max_y)
            if artifact.get_position().get_y() > robot.get_position().get_y()+5:
                cast.remove_actor("artifacts", artifact)
            if robot.get_position().y_is_between(artifact.get_position(), 1):
                cast.remove_actor("artifacts", artifact)
                message = artifact.get_message()
                if artifact.get_item_type() == "rock":
                    if self.points == 0:
                        artifact.set_message("Oops! That was a rock") 
                    else:
                        self.points -= 1
                        artifact.set_message("Oops! That was a rock") 
                elif artifact.get_item_type() == "gem":
                    self.points += 1
                    artifact.set_message("Nice!")
                elif artifact.get_item_type() == "asteroid":
                    self.points -= 2
                    artifact.set_message("Oops! That was an asteroid")
                banner.set_text("Score: " + str(self.points))  
                second_banner.set_text(artifact.get_message())
        
        if (self._video_service.get_time() - self.timer) > 0.7:
            self.timer=self._video_service.get_time()
            cast.add_actor("artifacts", cast.generate_random_item())
        

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
