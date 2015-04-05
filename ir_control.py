import platform, serial, irtoy, os, sys, picklereader

DEV_PATH = '/dev/'
defDev = '/dev/ttyACM0'
linux_based = True

ir_signals = dict()

dev_list = os.listdir(DEV_PATH)
devs_used = []


def loadAvailIrSignals():
    return picklereader.load_obj('signals')


def diffSignals(a, b):
    i=0
    res = {}
    lena, lenb = len(a), len(b)
    print lena, lenb
    res['lenMatch'] = {'bool': lenb == lena, 'len_a': lena, 'len_b': lenb}

    if lena > lenb:
        tmp = b
        b = a
        a = b

    for aa in a:
        if not aa is b[i]:
            res[i] = abs(aa - b[i])
        i+=1
    return res

def findSignalInAvailIrSignals(signal):
    global ir_signals
    if ir_signals:
        for key, data in ir_signals.items():
            print key

            res=diffSignals(data, signal)
            #res = list(set(signal) - set(data))
            print res
            if res['lenMatch']['bool']:
                res['matching_signal'] = key
                return res
    return 'NoMatch'

class IrController:
    dev = ''
    toy = None

    def __init__(self, isTransmitter=True):
        if not isinstance(isTransmitter, bool):
            isTransmitter = False
        self.toy = self.getToy(isTransmitter)

        if self.toy is None:
            raise Exception("Could not get hold of a irtoy!")

        self.dev  = self.toy.toy.getPort()

        if platform.win32_ver()[0] or self.dev is '':
            sys.exit(0)

    @staticmethod
    def findUsbSerialDevice(devtype='ttyACM'):
        global dev_list
        return [item for item in dev_list if item.startswith(devtype)]

    @staticmethod
    def getSerialDevice(nr=0):
        global linux_based, devs_used, defDev

        # if nr is 0:
        #     nr = len(devs_used)

        if linux_based:
            print defDev
        else:
            try:
                dev = IrController.findUsbSerialDevice('tty.usbmodem')[nr]
                dev = DEV_PATH + dev
            except IndexError:
                dev = ''
                print 'The', nr, 'th device is not available'
                return None

        if dev in devs_used:
            return None

        s = serial.Serial(dev)
        devs_used.append(dev)
        print "Linux based:", linux_based, "dev:", dev
        return s

    @staticmethod
    def getToy(t=True):
        if t:
            s = IrController.getSerialDevice()
        else:
            s = IrController.getSerialDevice(1)

        if s is None:
            print "The device is already in use!"
            return s
        return irtoy.IrToy(s)


if not platform.linux_distribution()[0]:
    linux_based = False

#tdev = getSerialDevice()
#rdev = getSerialDevice(1)


ir_signals = loadAvailIrSignals()

#toy = getToy()

#if __main__ == "__main__":
#    print "MAIN"