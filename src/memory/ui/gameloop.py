from .renderer import Renderer
from .clock import Clock
from .eventhandler import EventHandler

class GameLoop:
    """
    The pygame loop.

    Attributes:
        system: A LevelService or Menu object.
        window: The window to be used.
        clock: Pygame clock.
        renderer: Renderer object that renders images.
        event_handler: EventHandler object.
    """
    def __init__(self, system, window, save):
        """
        Constructs a new GameLoop object.

        Args:
            system: A LevelService or Menu object.
            window: The window to be used.
            save: The leaderboard.
        """
        self.system = system
        self.window = window
        self.clock = Clock()
        self.renderer = Renderer(self.window, self.system, save)
        self.event_handler = EventHandler(self.system)

    def loop(self):
        """
        The pygame loop itself.
        """
        while True:
            event = self.event_handler.handle_events()
            if event is False:
                exit()
            if event is not None:
                return event
            self.renderer.render()
            self.clock.tick()
