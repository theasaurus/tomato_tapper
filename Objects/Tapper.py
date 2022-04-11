from GameFrame import RoomObject, Globals
from math import ceil


class Tapper(RoomObject):
    def __init__(self, room, x, y, sound):
        RoomObject.__init__(self, room, x, y)

        self.tapper_can_buy = self.load_image('tapper_can_buy.png')
        self.tapper_no_buy = self.load_image('tapper_no_buy.png')
        self.set_image(self.tapper_no_buy, 96, 96)

        self.can_buy = False

        self.buy_sound = sound

        self.handle_mouse_events = True

        self.set_timer(1, self.buy)

    def clicked(self, button_number):
        if self.can_buy:
            Globals.SCORE -= Globals.tapper_cost
            Globals.tapper_cost = ceil(Globals.tapper_cost * 1.8)
            Globals.tps += 1
            self.buy_sound.play()

    def buy(self):
        if Globals.SCORE >= Globals.tapper_cost:
            self.can_buy = True
            self.set_image(self.tapper_can_buy, 96, 96)
        else:
            self.can_buy = False
            self.set_image(self.tapper_no_buy, 96, 96)
        self.set_timer(1, self.buy)
