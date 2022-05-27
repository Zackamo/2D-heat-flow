import numpy as np
import matplotlib.pyplot as plt

data_file = open("data_exp_1.txt", 'r')
lines = data_file.readlines()

rows, cols = (9, 9)
arr = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)

timestep = 0
all_temps = []
all_x = []
all_y = []
temps = []
x = []
y = []

for line in lines:
    words = line.split()
    if len(words) > 0 and words[0] == "Timestep:":
        timestep = words[1]
    elif len(words) > 0:
        values = line.split(",")
        x.append(values[0])
        y.append(values[1])
        temps.append(str.strip(values[2]))
        if int(values[0]) == 8 and int(values[1]) == 8:
            all_temps.append(temps)
            all_x.append(x)
            all_y.append(y)
            x = []
            y = []
            temps = []

print(all_temps)
print(all_x)
print(all_y)
print(timestep)

rows, cols = (9, 9)
arr = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)
sensor_temp = []
for i in (range(len(all_temps))):
    for j in range(0, 81):
        xPos = int(all_x[i][j])
        yPos = int(all_y[i][j])
        T = all_temps[i][j]
        arr[yPos][xPos] = T
        if xPos == 8 and yPos == 8:
            mynorm = plt.Normalize(vmin=21, vmax=22)
            plt.imshow(arr, cmap = "rainbow", norm = mynorm, interpolation="gaussian")
            plt.colorbar()
            plt.title("Timestep: " + str(i))
            #plt.show()
            plt.savefig("exp_" + str(i) + "_.png")
            plt.close()
        if xPos == 4 and yPos == 4:
            sensor_temp.append(T)

time_steps = np.arange(0, int(timestep) + 1, 1)
plt.scatter(time_steps, sensor_temp)
plt.xlabel("Time (s)")
plt.ylabel('Temperature (\N{DEGREE SIGN}C)')
plt.show()

