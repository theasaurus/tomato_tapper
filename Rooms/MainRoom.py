from GameFrame import Level, TextObject, Globals
from Objects import Tomato, Tapper


class MainRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # Load in images and sound
        self.set_background_image('kitchen.jpg')
        self.buy_sound = self.load_sound('buy.wav')

        # Create text objects
        # score = number of tomatoes
        self.score = TextObject(self, 300, 20, str(Globals.SCORE), 50)
        # tps = tomatoes per second added to the score
        self.tps = TextObject(self, 335, 76, str(Globals.tps), 20)
        # cost = number of tomatoes to buy a tapper
        self.cost = TextObject(self, 600, 500, str(Globals.tapper_cost), 20)

        # Add tomato, tapper and text
        self.add_room_object(Tomato(self, 150, 150))
        self.add_room_object(Tapper(self, 600, 400, self.buy_sound))
        self.add_room_object(self.score)
        self.add_room_object(self.tps)
        self.add_room_object(self.cost)

        # Set timers - update score every tick, update tomatoes every second (30 ticks)
        self.set_timer(1, self.update_all_text)
        self.set_timer(30, self.increase_score)

    # Update the text on the screen every tick
    def update_all_text(self):
        self.score.text = str(Globals.SCORE)
        self.score.update_text()
        self.tps.text = str(Globals.tps)
        self.tps.update_text()
        self.cost.text = "Cost: " + str(Globals.tapper_cost)
        self.cost.update_text()
        self.set_timer(1, self.update_all_text)

    # Increase the score by the amount of tomatoes per second we have
    def increase_score(self):
        Globals.SCORE += Globals.tps
        self.set_timer(30, self.increase_score)




