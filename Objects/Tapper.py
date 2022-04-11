from GameFrame import RoomObject, Globals
from math import ceil


class Tapper(RoomObject):
    def __init__(self, room, x, y, sound):
        RoomObject.__init__(self, room, x, y)

        # Load in images
        self.tapper_can_buy = self.load_image('tapper_can_buy.png')
        self.tapper_no_buy = self.load_image('tapper_no_buy.png')

        # Set image and sound
        self.set_image(self.tapper_no_buy, 96, 96)
        self.buy_sound = sound

        # True if you can afford a tapper
        self.can_buy = False

        self.handle_mouse_events = True

        # Check if we can buy a tapper every tick
        self.set_timer(1, self.check_buy)

    def clicked(self, button_number):
        if self.can_buy:
            Globals.SCORE -= Globals.tapper_cost
            # Increase the cost of the tapper each time it is bought - ceil rounds up to nearest integer
            Globals.tapper_cost = ceil(Globals.tapper_cost * 1.8)
            # Increase the amount of tomatoes generated per second
            Globals.tps += 1
            self.buy_sound.play()

    # Check if the tapper can be bought every tick
    def check_buy(self):
        if Globals.SCORE >= Globals.tapper_cost:
            self.can_buy = True
            self.set_image(self.tapper_can_buy, 96, 96)
        else:
            self.can_buy = False
            self.set_image(self.tapper_no_buy, 96, 96)
        self.set_timer(1, self.check_buy)
