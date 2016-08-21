#!/usr/bin/env python

import uinput
import random
import time 
from random import randrange

#every 30-50 seconds the script press the right key 
while 1:
    wait = randrange(30, 50)
    time.sleep(wait)
    device = uinput.Device([
            uinput.KEY_RIGHT
            ])

    device.emit_combo([
            uinput.KEY_RIGHT
            ])
