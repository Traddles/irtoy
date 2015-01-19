# irtoy
This is for the irpart of the DOME-project

# use
from irtoy import IrToy
import serial

serialDevice = serial.Serial('/dev/ttyACM0')

toy = IrToy(serialDevice)

