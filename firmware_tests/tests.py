import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)

ser = ''

try:
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600
    )
except serial.serialutil.SerialException:
    ser = serial.Serial(
        port='/dev/ttyACM1',
        baudrate=9600
    )

ser.isOpen()

tmp = 0


def down_and_up(tmp):
    if tmp == 0:
        ser.write('M300S50\r\n')
        tmp = 1
    else:
        if tmp == 1:
            ser.write('M300S30\r\n')
            tmp = 0
    return tmp

def square():
    ser.write('M300S30 G1X0Y0 G1X30Y0 G1X30Y30 G1X0Y30 G1X0\r\n')


def homing():
    ser.write('M300S30 G1X0Y0 G1X50Y50 G1X0Y0\r\n')
    
def down_and_up_once():
    ser.write('M300S30 G4 P300 M300S50\r\n')

while 1 :
#  //  G1 for moving
#  //  G4 P300 (wait 150ms)
#  //  G1 X60 Y30
#  //  G1 X30 Y50
#  //  M300 S30 (pen down)
#  //  M300 S50 (pen up)
#  //  Discard anything with a (
#  //  Discard any other command!
    #

    #tmp = down_and_up(tmp)
    homing()
    #down_and_up_once()
    
    #ser.write('G1X0Y0 G1X100Y100\r\n')
    
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out != '':
        print ">>" + out
    time.sleep(25)
