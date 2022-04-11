from GameFrame import Level, TextObject, Globals
from Objects import Tomato, Tapper


class MainRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("kitchen.jpg")

        self.add_room_object(Tomato(self, 150, 150))

        self.add_room_object(Tapper(self, 600, 400))

        self.score = TextObject(self, 300, 30, str(Globals.SCORE), 50)
        self.add_room_object(self.score)
        self.tps = TextObject(self, 335, 84, str(Globals.tps), 20)
        self.add_room_object(self.tps)

        self.set_timer(1, self.update_score)
        self.set_timer(30, self.increase_score)

    def update_score(self):
        self.score.text = str(Globals.SCORE)
        self.score.update_text()
        self.tps.text = str(Globals.tps)
        self.tps.update_text()
        self.set_timer(1, self.update_score)

    def increase_score(self):
        Globals.SCORE += Globals.tps
        self.set_timer(30, self.increase_score)




