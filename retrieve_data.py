import serial
import matplotlib.pyplot as plt


# THIS IS DATA FROM ARDUINO
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=serial.EIGHTBITS
)

while (True):
  if (ser.inWaiting()):
    data = ser.read(ser.inWaiting())
    if (data[-1] == '|'):
      print(ser.inWaiting())
      print(data)

ser.close()