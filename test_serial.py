import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(2)

ser.write(b'1\n')
time.sleep(2)

ser.write(b'0\n')

ser.close()
