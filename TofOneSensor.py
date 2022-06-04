import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import chisquare

TRIAL = 8
exp_data = open("data_exp_" + str(TRIAL) + ".txt", 'r')
comp_data = open("data_comp_" + str(TRIAL) + ".txt", 'r')

exp_lines = exp_data.readlines()
comp_lines = comp_data.readlines()

exp_sensor_22 = []
exp_sensor_26 = []
exp_sensor_62 = []
exp_sensor_66 = []
exp_sensor_44 = []

comp_sensor_22 = []
comp_sensor_26 = []
comp_sensor_62 = []
comp_sensor_66 = []
comp_sensor_44 = []

for i in exp_lines:
    #print(i)
    values = i.split(",")
    #print(values)
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 6:
        #print(values[2])
        exp_sensor_26.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 2:
        #print(values[2])
        exp_sensor_22.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 2:
        #print(values[2])
        exp_sensor_62.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 6:
        #print(values[2])
        exp_sensor_66.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 4 and int(values[1]) == 4:
        exp_sensor_44.append(float(str.strip(values[2])))

for i in comp_lines:
    #print(i)
    values = i.split(",")
    #print(values)
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 6:
        #print(values[2])
        comp_sensor_26.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 2 and int(values[1]) == 2:
        #print(values[2])
        comp_sensor_22.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 2:
        #print(values[2])
        comp_sensor_62.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 6 and int(values[1]) == 6:
        #print(values[2])
        comp_sensor_66.append(float(str.strip(values[2])))
    if len(values) > 1 and int(values[0]) == 4 and int(values[1]) == 4:
        #print(values[2])
        comp_sensor_44.append(float(str.strip(values[2])))

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
print(len(comp_sensor_22[0:90]))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.scatter(x, exp_sensor_62[0:90], label = "Experimental (6, 2)", color = "green")
ax.scatter(x, exp_sensor_22[0:90], label = "Experimental (2, 2)", color = "brown")
ax.scatter(x, exp_sensor_26[0:90], label = "Experimental (2, 6)", color = "orange")
ax.scatter(x, exp_sensor_66[0:90], label = "Experimental (6, 6)", color = "purple")
#ax.scatter(x, exp_sensor_44[0:90], label = "Experimental (4, 4)", color = "brown")

ax.scatter(x, comp_sensor_62[0:90], label = "Computational (6, 2)", marker = "*", color = "green")
ax.scatter(x, comp_sensor_22[0:90], label = "Computational (2, 2)", marker = "*", color = "brown")
ax.scatter(x, comp_sensor_26[0:90], label = "Computational (2, 6)", marker = "*", color = "orange")
ax.scatter(x, comp_sensor_66[0:90], label = "Computational (6, 6)", marker = "*", color = "purple")
#ax.scatter(x, comp_sensor_44[0:90], label = "Computational (4, 4)", marker = "*", color = "brown")

plt.axhline(y=18, color='r', linestyle='--')

#ax.scatter(x, comp_sensor[0:90], label = "Computational")
plt.legend()
ax.set_xlabel('Timestep (s)', fontsize = 16)
ax.set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 16)
ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
ax.set_xticklabels(['0', '15', '30', '45', '60', '75', '90'], Fontsize = 14)
ax.set_yticks([10, 15, 20, 25])
ax.set_yticklabels(['10', '15', '20', '25'], Fontsize = 14)
#ax.set_yticks([5, 10, 15, 20, 25, 30])
#ax.set_yticklabels(['5', '10', '15', '20', '25', '30'], Fontsize = 14)
plt.show()

print(chisquare(exp_sensor_22[0:90], f_exp=comp_sensor_22[0:90]))
print(chisquare(exp_sensor_26[0:90], f_exp=comp_sensor_26[0:90]))
print(chisquare(exp_sensor_62[0:90], f_exp=comp_sensor_62[0:90]))
print(chisquare(exp_sensor_66[0:90], f_exp=comp_sensor_66[0:90]))




