from GameFrame import Level
from Objects import Tomato


class MainRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("kitchen.jpg")

        self.add_room_object(Tomato(self, 150, 150))
