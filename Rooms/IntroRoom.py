from GameFrame import Level
from Objects import PlayButton


class IntroRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('title.png')

        self.add_room_object(PlayButton(self, 200, 200))
