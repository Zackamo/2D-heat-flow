import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import chisquare

TRIAL = 8
exp_data = open("data_exp_" + str(TRIAL) + ".txt", 'r')
comp_data = open("data_comp_" + str(TRIAL) + ".txt", 'r')

exp_lines = exp_data.readlines()
comp_lines = comp_data.readlines()

exp = []
current_exp = []
for i in exp_lines:
    values = i.split(",")
    if (len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 8):
        current_exp.append(float(str.strip(values[2])))
        exp.append(current_exp)
        current_exp = []
    elif (len(values) > 1):
        current_exp.append(float(str.strip(values[2])))

exp_mean = []
exp_std = []

for i in exp:
    exp_mean.append(sum(i)/len(i))
    variance = sum([((x - sum(i)/len(i)) ** 2) for x in i]) / len(i)
    res = variance ** 0.5
    exp_std.append(res)

comp = []
current_comp = []
for i in comp_lines:
    values = i.split(",")
    if (len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 8):
        current_comp.append(float(str.strip(values[2])))
        comp.append(current_comp)
        current_comp = []
    elif (len(values) > 1):
        current_comp.append(float(str.strip(values[2])))

comp_mean = []
comp_std = []

for i in comp:
    comp_mean.append(sum(i)/len(i))
    variance = sum([((x - sum(i)/len(i)) ** 2) for x in i]) / len(i)
    res = variance ** 0.5
    comp_std.append(res)

TRIAL = 6
exp_data2 = open("data_exp_" + str(TRIAL) + ".txt", 'r')
comp_data2 = open("data_comp_" + str(TRIAL) + ".txt", 'r')

exp_lines2 = exp_data2.readlines()
comp_lines2 = comp_data2.readlines()

exp2 = []
current_exp2 = []
for i in exp_lines2:
    values = i.split(",")
    if (len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 8):
        current_exp2.append(float(str.strip(values[2])))
        exp2.append(current_exp2)
        current_exp2 = []
    elif (len(values) > 1):
        current_exp2.append(float(str.strip(values[2])))

exp_mean2 = []
exp_std2 = []

for i in exp2:
    exp_mean2.append(sum(i)/len(i))
    variance = sum([((x - sum(i)/len(i)) ** 2) for x in i]) / len(i)
    res = variance ** 0.5
    exp_std2.append(res)

comp2 = []
current_comp2 = []
for i in comp_lines2:
    values = i.split(",")
    if (len(values) > 1 and int(values[0]) == 8 and int(values[1]) == 8):
        current_comp2.append(float(str.strip(values[2])))
        comp2.append(current_comp2)
        current_comp2 = []
    elif (len(values) > 1):
        current_comp2.append(float(str.strip(values[2])))

comp_mean2 = []
comp_std2 = []

for i in comp2:
    comp_mean2.append(sum(i)/len(i))
    variance = sum([((x - sum(i)/len(i)) ** 2) for x in i]) / len(i)
    res = variance ** 0.5
    comp_std2.append(res)

timesteps = np.arange(1, 91, 1)
print(timesteps)
#print(exp_sensor)
#print(comp_sensor)

print(exp_mean == exp_mean2)

print(comp_mean[0:90])
print(comp_mean2[0:90])
print(exp_std[0:90])
print(exp_std2[0:90])


x = timesteps
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.scatter(x, exp_mean[0:90], label = u"\u03bc of Exp Data (Config 1)", color = "green")
ax.scatter(x, comp_mean[0:90], label = u"\u03bc of Comp Data (Config 1)", color = "green", marker = "*")
ax.scatter(x, exp_mean2[0:90], label = u"\u03bc of Exp Data (Config 2)", color = "orange")
ax.scatter(x, comp_mean2[0:90], label = u"\u03bc of Comp Data (Config 1)", color = "orange", marker = "*")
plt.legend()
ax.set_xlabel('Timestep (s)', fontsize = 16)
ax.set_ylabel('Mean Temperature (\N{DEGREE SIGN}C)', fontsize = 16)
ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
ax.set_xticklabels(['0', '15', '30', '45', '60', '75', '90'], Fontsize = 14)
ax.set_yticks([17, 18, 19])
ax.set_yticklabels(['17', '18', '19'], Fontsize = 14)
#ax.set_yticks([5, 10, 15, 20, 25, 30])
#ax.set_yticklabels(['5', '10', '15', '20', '25', '30'], Fontsize = 14)
plt.show()

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.scatter(x, exp_std[0:90], label = u"\u03C3$^2$ of Exp Data (Config 1)", color = "green")
ax.scatter(x, comp_std[0:90], label = u"\u03C3$^2$ of Comp Data (Config 1)", color = "green", marker = "*")
ax.scatter(x, exp_std2[0:90], label = u"\u03C3$^2$ of Exp Data (Config 2)", color = "orange")
ax.scatter(x, comp_std2[0:90], label = u"\u03C3$^2$ of Comp Data (Config 1)", color = "orange", marker = "*")
plt.legend()
ax.set_xlabel('Timestep (s)', fontsize = 16)
ax.set_ylabel('Std Dev of Temperature (\N{DEGREE SIGN}C)', fontsize = 16)
ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
ax.set_xticklabels(['0', '15', '30', '45', '60', '75', '90'], Fontsize = 14)
ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.set_yticklabels(['0', '2', '4', '6', '8', '10'], Fontsize = 14)
#ax.set_yticks([5, 10, 15, 20, 25, 30])
#ax.set_yticklabels(['5', '10', '15', '20', '25', '30'], Fontsize = 14)
plt.show()
