from GameFrame import Level, TextObject, Globals
from Objects import Tomato


class MainRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("kitchen.jpg")

        self.add_room_object(Tomato(self, 150, 150))

        self.score = TextObject(self, 300, 30, str(Globals.SCORE), 50)
        self.add_room_object(self.score)

        self.set_timer(1, self.update_score)

    def update_score(self):
        self.score.text = str(Globals.SCORE)
        self.score.update_text()
        self.set_timer(1, self.update_score)




