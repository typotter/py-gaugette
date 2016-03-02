import wiringpi2
import gaugette.gpio as gpio


class Switch:

    def __init__(self, pin, pullUp=True):
        self.pin = pin
        self.pullUp = pullUp
        
        print "b %s" % gpio
        self.gpio = gpio.get_instance().gpio
        self.gpio.pinMode(self.pin, self.gpio.INPUT)
        if self.pullUp:
            self.gpio.pullUpDnControl(self.pin, self.gpio.PUD_UP)
        else:
            self.gpio.pullUpDnControl(self.pin, self.gpio.PUD_DOWN)

    def get_state(self):
        state = self.gpio.digitalRead(self.pin)
        if self.pullUp:
            # If we are pulling up and switching
            # to ground, state will be 1 when the switch is open, and 0
            # when it is closed.  We invert the value here to a more
            # conventional representation of 0:open, 1:closed.
            return 1-state
        else:
            return state
