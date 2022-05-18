import serial
import numpy as np
import matplotlib.pyplot as plt

def split(word):
    return [char for char in word]

# THIS IS DATA FROM ARDUINO
ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    bytesize=serial.EIGHTBITS
)

all_data = []
flag = True
data = ''
error_string = ''
data_flag = False

while(flag):
    if (ser.inWaiting()):
        character = ser.read(1)
        ascii_char = chr(character[0])

        if (ascii_char == '&'):
            data_flag = True

        elif (data_flag):
            if (ascii_char == '|'):
                data_flag = False
                if len(data) > 0:
                    all_data.append(str.strip(data))
                data = ''
            else:
                data = data + str(ascii_char)
                #print("data: " + str(data))

        else:
            error_string = error_string + str(ascii_char)
            if "End of timestep" in error_string:
                flag = False
            #print("ascii_char: " + str(ascii_char))
            #print("data: " + str(error_string))
        #print(all_data)

print("all_data: " + str(all_data))
print("END")

all_time_steps = []
x = []
y = []
temps = []

t_arr=np.linspace(0,5,1)
for i in all_data:
    values = i.split(",")
    x.append(values[0])
    y.append(values[1])
    temps.append(values[2])

all_time_steps.append(temps)

print(x)
print(y)
print(temps)
print(all_time_steps)


ser.close()