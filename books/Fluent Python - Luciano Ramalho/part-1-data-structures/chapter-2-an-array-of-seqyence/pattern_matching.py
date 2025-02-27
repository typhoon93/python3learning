"""
The expression after the match keyword is the subject. The subject is the data that
Python will try to match to the patterns in each case clause.
This pattern matches any subject that is a sequence with three items. The first
item must be the string 'BEEPER'. The second and third item can be anything,
and they will be bound to the variables frequency and times, in that order.
This matches any subject with two items, the first being 'NECK'.
This will match a subject with three items starting with 'LED'. If the number of
items does not match, Python proceeds to the next case.
Another sequence pattern starting with 'LED', now with five items—including
the 'LED' constant.
"""


class InvalidCommand:
    pass


def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
        case _:
            raise InvalidCommand(message)
