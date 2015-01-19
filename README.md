# irtoy
This is for the irpart of the DOME-project

# get right serial id (ubuntu)
dmesg | grep tty

# use
from irtoy import IrToy

import serial

serialDevice = serial.Serial('/dev/ttyACM0')

toy = IrToy(serialDevice)

