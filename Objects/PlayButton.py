from GameFrame import RoomObject


class PlayButton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # Set image
        button_image = self.load_image('tomato_button.png')
        self.set_image(button_image, 372, 347)

        self.handle_mouse_events = True

    # When clicked, go to the next room (MainRoom)
    def clicked(self, button_number):
        self.room.running = False
