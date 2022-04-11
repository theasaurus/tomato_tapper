from GameFrame import RoomObject, Globals


class Tapper(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        tapper_icon = self.load_image('tapper.png')
        self.set_image(tapper_icon, 96, 96)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        Globals.tps += 1
