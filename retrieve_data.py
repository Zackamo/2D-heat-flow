import serial
import numpy as np
import matplotlib.pyplot as plt

#3 is heatgun at top right
#4 is dry ice at bottom right
#5 heat gun top left, dry ice bottom right
#6 heat gun top right, dry ice bottom right
#7 Time step test
#8 heat gun top left, dry ice bottom right, recollect with heat gun pointing away from dry ice
TRIAL = 8

def split(word):
    return [char for char in word]

# THIS IS DATA FROM ARDUINO
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=serial.EIGHTBITS
)

all_data = []
flag = True
data = ''
error_string = ''
data_flag = False

data_file = open("data_exp_" + str(TRIAL) + ".txt", 'w')

i = 0
num_time_steps = 180

data_file.write("Timestep: " + str(i) + " s\n")

while(i < num_time_steps):
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
                    data_file.write(str.strip(data) + '\n')
                data = ''
            else:
                data = data + str(ascii_char)

        else:
            error_string = error_string + str(ascii_char)
            if "End of timestep" in error_string:
                error_string = ''
                i += 1
                if (i < num_time_steps):
                    data_file.write("\nTimestep: " + str(i) + " s\n")

print("all_data: " + str(all_data))
print("END")

data_file.close()

all_time_steps = []
all_x = []
all_y = []
x = []
y = []
temps = []

min_temp = 50
max_temp = 0


for i in all_data:
    values = i.split(",")
    x.append(values[0])
    y.append(values[1])
    temps.append(values[2])
    if float(values[2]) > max_temp:
        max_temp = values[2]

    if float(values[2]) < min_temp:
        min_temp = values[2]

    if int(values[0]) == 8 and int(values[1]) == 8:
        all_time_steps.append(temps)
        all_x.append(x)
        all_y.append(y)
        x = []
        y = []
        temps = []

print(min_temp)
print(max_temp)

ser.close()

rows, cols = (9, 9)
arr = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)
#mynorm = plt.Normalize(vmin=10, vmax=50)
#plt.imshow(arr, cmap = "plasma", norm = mynorm)
#plt.show()
sensor_temp = []
for i in (range(len(all_time_steps))):
    for j in range(0, 81):
        xPos = int(all_x[i][j])
        yPos = int(all_y[i][j])
        T = all_time_steps[i][j]
        arr[yPos][xPos] = T
        if xPos == 8 and yPos == 8:
            mynorm = plt.Normalize(vmin=21, vmax=22)
            plt.imshow(arr, cmap = "rainbow", norm = mynorm, interpolation="gaussian")
            plt.colorbar()
            plt.title("Timestep: " + str(i))
            #plt.show()
            #plt.savefig("exp_" + str(i) + "_.png")
        if xPos == 4 and yPos == 4:
            sensor_temp.append(T)

time_steps = np.arange(1, num_time_steps + 1, 1)
plt.scatter(time_steps, sensor_temp)
plt.xlabel("Time (s)")
plt.ylabel('Temperature (\N{DEGREE SIGN}C)')
plt.show()

