import numpy as np
import matplotlib.pyplot as plt
import math
from IPython.display import clear_output
import tqdm
from tqdm import tqdm

data_file = open("data_exp_1.txt", 'r')
lines = data_file.readlines()
data_file_comp = open("data_comp_1.txt", 'w')

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

rho = 2710  # mass density
cp = 0.897  # heat capacity
k = 237  # thermal conductivity
n = 1500  # time steps
del_x = 0.29  # spatial step
del_t = 0.002
mesh_fourier_num = k * del_t / (cp * rho * del_x ** 2)

rows, cols = (11, 11)
arr_old = np.array([[20 for i in range(cols)] for j in range(rows)], dtype=float)
for i in all_x:
    for j in all_y:
        arr_old[int(i) + 1][int(j) + 1]=all_temps[9*int(i)+int(j)]

arr_new = arr_old.copy()

sensor_temp = []

for t in range(0, n):
    if t % 500 == 0:
        if t != 0:
            data_file_comp.write("\nTimestep: " + str(int(t * del_t)) + " s\n")
        else:
            data_file_comp.write("Timestep: " + str(int(t * del_t)) + " s\n")
        mynorm = plt.Normalize(vmin=21, vmax=22)
        plt.imshow(arr_new, cmap="rainbow", norm=mynorm, interpolation="gaussian")
        plt.title("Timestep: " + str(int(t*del_t)))
        plt.colorbar()
        #plt.show()
        plt.savefig("comp_" + str(int(t*del_t)) + "_.png")
        plt.close()
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            arr_new[x][y] = (1 - 4 * mesh_fourier_num) * arr_old[x][y] + mesh_fourier_num * (
                        arr_old[x + 1][y] + arr_old[x][y + 1] + arr_old[x - 1][y] + arr_old[x][y - 1])
            if x == 5 and y == 5:
                sensor_temp.append((1 - 4 * mesh_fourier_num) * arr_old[x][y] + mesh_fourier_num * (
                        arr_old[x + 1][y] + arr_old[x][y + 1] + arr_old[x - 1][y] + arr_old[x][y - 1]))

            if t % 500 == 0:
                data_file_comp.write(str(x - 1) + "," + str(y - 1) + "," + str(round(arr_old[x][y], 2)) + "\n")
    arr_old = arr_new

# print(arr_old)
# print(arr_new)
arr_truncated = arr_new
arr_truncated = np.delete(arr_truncated, (0), axis=1)
arr_truncated = np.delete(arr_truncated, (-1), axis=1)
arr_truncated = np.delete(arr_truncated, 0, axis=0)
arr_truncated = np.delete(arr_truncated, -1, axis=0)
# print(arr_truncated)
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








