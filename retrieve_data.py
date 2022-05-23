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
all_x = []
all_y = []
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
all_x.append(x)
all_y.append(y)

print(x)
print(y)
print(temps)
print(all_time_steps)
print(all_x)
print(all_y)

ser.close()

rows, cols = (9, 9)
arr = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)
arr[0, 8] = 0
plt.imshow(arr, cmap = "plasma")
plt.show()
for i in (range(len(all_time_steps))):
    for j in range(0, 81):
        xPos = int(all_x[i][j])
        yPos = int(all_y[i][j])
        T = all_time_steps[i][j]
        print(xPos)
        print(yPos)
        print(T)
        arr[xPos][yPos] = T
        if xPos == 8 and yPos == 8:
            plt.imshow(arr, cmap = "plasma")
            plt.show()




