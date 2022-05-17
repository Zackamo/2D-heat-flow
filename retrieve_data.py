import serial
import matplotlib.pyplot as plt

'''ser = serial.Serial('COM3', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
while True:
  data_raw = ser.readline()
  print(data_raw)'''


def split(word):
    return [char for char in word]

# THIS IS DATA FROM ARDUINO
ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    bytesize=serial.EIGHTBITS
)

all_data = []
while(True):
    data = ' '
    while (data[-1] != '|'):
      if (ser.inWaiting()):
        print(ser.inWaiting())
        line = ser.read(ser.inWaiting())
        s_line = split(line)
        print(split(line))
        for i in s_line:
            data += chr(i)

    print(data)
    all_data.append(data[1::])
    print(all_data)




ser.close()