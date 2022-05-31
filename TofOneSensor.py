import matplotlib.pyplot as plt
import numpy as np
import math

TRIAL = 8
exp_data = open("data_exp_" + str(TRIAL) + ".txt", 'r')
comp_data = open("data_comp_" + str(TRIAL) + ".txt", 'r')

exp_lines = exp_data.readlines()
comp_lines = comp_data.readlines()

exp_sensor_22 = []
exp_sensor_26 = []
exp_sensor_62 = []
exp_sensor_66 = []

comp_sensor_22 = []
comp_sensor_26 = []
comp_sensor_62 = []
comp_sensor_66 = []

for i in exp_lines:
    print(i)
    values = i.split(",")
    print(values)
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 6:
        print(values[2])
        exp_sensor_26.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 2:
        print(values[2])
        exp_sensor_22.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 2:
        print(values[2])
        exp_sensor_62.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 6:
        print(values[2])
        exp_sensor_66.append(float(str.strip(values[2])))

for i in comp_lines:
    print(i)
    values = i.split(",")
    print(values)
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 6:
        print(values[2])
        comp_sensor_26.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 2:
        print(values[2])
        comp_sensor_22.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 2:
        print(values[2])
        comp_sensor_62.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 6:
        print(values[2])
        comp_sensor_66.append(float(str.strip(values[2])))

'''comp_sensor = []
for i in comp_lines:
    print(i)
    values = i.split(",")
    print(values)
    if len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 8:
        print(values[2])
        comp_sensor.append(float(str.strip(values[2])))'''

timesteps = np.arange(1, 91, 1)
print(timesteps)
#print(exp_sensor)
#print(comp_sensor)

x = timesteps
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.scatter(x, exp_sensor_22[0:90], label = "Experimental_22")
ax.scatter(x, exp_sensor_26[0:90], label = "Experimental_26")
ax.scatter(x, exp_sensor_62[0:90], label = "Experimental_62")
ax.scatter(x, exp_sensor_66[0:90], label = "Experimental_66")
ax.scatter(x, comp_sensor_22[0:90], label = "Computational_22")
ax.scatter(x, comp_sensor_26[0:90], label = "Computational_26")
ax.scatter(x, comp_sensor_62[0:90], label = "Computational_62")
ax.scatter(x, comp_sensor_66[0:90], label = "Computational_66")
plt.axhline(y=18, color='r', linestyle='-')

#ax.scatter(x, comp_sensor[0:90], label = "Computational")
plt.legend()
ax.set_xlabel('Timestep (s)', fontsize = 16)
ax.set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 16)
ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
ax.set_xticklabels(['0', '15', '30', '45', '60', '75', '90'], Fontsize = 14)
ax.set_yticks([20, 21, 22, 23, 24, 25])
ax.set_yticklabels(['20', '21', '22', '23', '24', '25'], Fontsize = 14)
plt.text(0.08, 0.2, 'sin')
plt.text(0.9, 0.2, 'cos')
plt.show()


