# irtoy test pahi
This is for the irpart of the DOME-project

## get right serial id (ubuntu)
dmesg | grep tty

## search serial id (mac)
dmesg | grep ACM

tail -f /var/log/system.log

## allow serial device access
sudo chmod 777 /dev/ttyACM0

## use
from irtoy import IrToy

import serial

serialDevice = serial.Serial('/dev/ttyACM0')

toy = IrToy(serialDevice)

## test irtoy
https://github.com/crleblanc/PyIrToy/blob/master/tests/test_irtoy.py
