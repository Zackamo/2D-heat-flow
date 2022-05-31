import matplotlib.pyplot as plt
import numpy as np
import math

TRIAL = 3
exp_data = open("data_exp_" + str(TRIAL) + ".txt", 'r')
comp_data = open("data_comp_" + str(TRIAL) + ".txt", 'r')

exp_lines = exp_data.readlines()
comp_lines = comp_data.readlines()

exp_sensor = []
for i in exp_lines:
    print(i)
    values = i.split(",")
    print(values)
    if len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 0:
        print(values[2])
        exp_sensor.append(float(str.strip(values[2])))

comp_sensor = []
for i in comp_lines:
    print(i)
    values = i.split(",")
    print(values)
    if len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 0:
        print(values[2])
        comp_sensor.append(float(str.strip(values[2])))

timesteps = np.arange(1, 91, 1)
print(timesteps)
print(exp_sensor)
print(comp_sensor)

x = timesteps
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.scatter(x, exp_sensor[0:90], label = "Experimental")
ax.scatter(x, comp_sensor[0:90], label = "Computational")
ax.set_xlabel('Timestep (s)', fontsize = 16)
ax.set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 16)
ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
ax.set_xticklabels(['0', '15', '30', '45', '60', '75', '90'], Fontsize = 14)
#ax.set_xticklabels(['zero','two','four','six'])
ax.set_yticks([20, 25, 30, 35, 40])
ax.set_yticklabels(['20', '25', '30', '35', '40'], Fontsize = 14)
plt.text(0.08, 0.2, 'sin')
plt.text(0.9, 0.2, 'cos')
plt.show()


