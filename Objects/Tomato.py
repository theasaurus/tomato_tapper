from GameFrame import RoomObject, Globals


class Tomato(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        tomato_image = self.load_image("tomato_game.png")
        self.set_image(tomato_image, 372, 347)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        Globals.SCORE += 1

