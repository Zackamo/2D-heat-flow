import numpy as np
import matplotlib.pyplot as plt
import math
from IPython.display import clear_output
import tqdm
from tqdm import tqdm
TRIAL = 6
data_file = open("data_exp_" + str(TRIAL) + ".txt", 'r')
lines = data_file.readlines()
data_file_comp = open("data_comp_" + str(TRIAL) + ".txt", 'w')

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

all_temps = all_temps[0]
all_x = all_x[0]
all_y = all_y[0]

rho = 2710  # mass density 2710
cp = 0.897  # heat capacity 0.897
k = 237  # thermal conductivity
n = 90000  # time steps
del_x = 0.29  # spatial step
del_t = 0.002
mesh_fourier_num = k * del_t / (cp * rho * del_x ** 2)

rows, cols = (11, 11)
arr_old = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)
for i in all_x:
    for j in all_y:
        arr_old[int(j) + 1][int(i) + 1]=all_temps[9*int(i)+int(j)]
for x in range(cols):
    for y in range(cols):
        #print(arr_old[y][x])
        if (x == 0):
            arr_old[y][x] = arr_old[y][x+1]
        if (x == 10):
            arr_old[y][x] = arr_old[y][x-1]
        if (y == 0):
            arr_old[y][x] = arr_old[y+1][x]
        if (y == 10):
            arr_old[y][x] = arr_old[y-1][x]
        if (x == 0 and y == 0):
            arr_old[y][x] = arr_old[y+1][x+1]
        if (x == 10 and y == 0):
            arr_old[y][x] = arr_old[y][x-1]
arr_new = arr_old.copy()

sensor_temp = []

for t in range(0, n):
    print(t*del_t)
    if t % 2500 == 0:
        if t != 0:
            data_file_comp.write("\nTimestep: " + str(int(t * del_t)) + " s\n")
        else:
            data_file_comp.write("Timestep: " + str(int(t * del_t)) + " s\n")
        output = np.array([[0 for i in range(cols - 2)] for j in range(rows - 2)], dtype=float)
        num = 0
        for i in arr_old[1:-1]:
            output[num] = i[1:-1]
            num += 1
        mynorm = plt.Normalize(vmin=-15, vmax=40)
        plt.imshow(output, cmap="rainbow", norm=mynorm, interpolation="gaussian")
        cbar = plt.colorbar()
        cbar.set_label('\N{DEGREE SIGN} C', fontsize=12)
        plt.title("Timestep: " + str(int(t*del_t)))
        plt.xticks([0, 2, 4, 6, 8], fontsize=14)
        plt.yticks([0, 2, 4, 6, 8], fontsize=14)
        #plt.show()
        plt.savefig("comp_" + str(TRIAL) + "_" + str(int(t*del_t)) + "_.png")
        plt.close()
        print(output.round(2))
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            arr_new[y][x] = (1 - 4 * mesh_fourier_num) * arr_old[y][x] + mesh_fourier_num * (
                        arr_old[y + 1][x] + arr_old[y][x + 1] + arr_old[y - 1][x] + arr_old[y][x - 1])
            #print("arr_new")
            #print(arr_new)
            for x2 in range(cols):
                for y2 in range(cols):
                    # print(arr_old[y][x])
                    if (x2 == 0):
                        arr_new[y2][x2] = arr_new[y2][x2 + 1]
                    if (x2 == 10):
                        arr_new[y2][x2] = arr_new[y2][x2 - 1]
                    if (y2 == 0):
                        arr_new[y2][x2] = arr_new[y2 + 1][x2]
                    if (y2 == 10):
                        arr_new[y2][x2] = arr_new[y2 - 1][x2]
                    if (x2 == 0 and y2 == 0):
                        arr_new[y2][x2] = arr_new[y2 + 1][x2 + 1]
                    if (x2 == 10 and y2 == 0):
                        arr_new[y2][x2] = arr_new[y2][x2 - 1]
            #print("arr_new")
            #print(arr_new)
            if x == 5 and y == 5:
                sensor_temp.append((1 - 4 * mesh_fourier_num) * arr_old[y][x] + mesh_fourier_num * (
                        arr_old[y + 1][x] + arr_old[y][x + 1] + arr_old[y - 1][x] + arr_old[y][x - 1]))

            if t % 500 == 0:
                data_file_comp.write(str(x - 1) + "," + str(y - 1) + "," + str(round(arr_old[y][x], 2)) + "\n")
    arr_old = arr_new

arr_truncated = arr_new
arr_truncated = np.delete(arr_truncated, (0), axis=1)
arr_truncated = np.delete(arr_truncated, (-1), axis=1)
arr_truncated = np.delete(arr_truncated, 0, axis=0)
arr_truncated = np.delete(arr_truncated, -1, axis=0)
mynorm = plt.Normalize(vmin=10, vmax=50)
plt.imshow(arr_truncated, cmap="rainbow_r", norm = mynorm)
plt.colorbar()
#plt.savefig(str(n*del_t) + ".png")
plt.close()
temps = np.linspace(0, n * del_t, n)
plt.scatter(temps, sensor_temp)
plt.xlabel("Time (s)")
plt.ylabel('Temperature (\N{DEGREE SIGN}C)')

plt.show()








