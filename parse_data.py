import numpy as np
import matplotlib.pyplot as plt

TRIAL = 9
data_file = open("data_exp_" + str(TRIAL) + ".txt", 'r')
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

#print(all_temps)
#print(all_x)
#print(all_y)
#print(timestep)

rows, cols = (9, 9)
arr = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)
sensor_temp = []
for i in (range(len(all_temps))):
    print(i)
    for j in range(0, 81):
        xPos = int(all_x[i][j])
        yPos = int(all_y[i][j])
        T = all_temps[i][j]
        arr[yPos][xPos] = T
        #print(arr)
        if xPos == 8 and yPos == 8:
            if (i % 5 == 0 or i == 0):
                print("in if")
                print(i)
                mynorm = plt.Normalize(vmin=-15, vmax=40)
                plt.imshow(arr, cmap = "rainbow", norm = mynorm, interpolation="gaussian")
                cbar = plt.colorbar()
                cbar.set_label('\N{DEGREE SIGN} C', fontsize=12)
                plt.title("Timestep: " + str(i))
                plt.xticks([0, 2, 4, 6, 8], fontsize=14)
                plt.yticks([0, 2, 4, 6, 8], fontsize=14)
                plt.savefig("exp_" + str(TRIAL) + "_" + str(i) + "_.png")
                print(i*3)
                plt.close()
                plt.show()
        if xPos == 4 and yPos == 4:
            sensor_temp.append(T)

