# irtoy test pahi
This is for the irpart of the DOME-project

## get right serial id (ubuntu)
dmesg | grep tty

## allow serial device access
sudo chmod 777 /dev/ttyACM0

## use
from irtoy import IrToy

import serial

serialDevice = serial.Serial('/dev/ttyACM0')

toy = IrToy(serialDevice)

