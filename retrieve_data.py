import serial
import matplotlib.pyplot as plt

def split(word):
    return [char for char in word]

# THIS IS DATA FROM ARDUINO
ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    bytesize=serial.EIGHTBITS
)

'''all_data = []
i = 0
data = ""
while(True):
    if (ser.inWaiting()):
        line = ser.read(ser.inWaiting())
        print(line)
        split = line.split()
        print(split)
        for i in line:
            if i == "|":
                print(data)
                all_data.append(data)
                data = ''
            else:
                print(chr(i))
                data += chr(i)
    i += 1

print(all_data)

print("//////////////////////////////////////")'''

all_data = []

i = 0
flag = True
while(flag):
    data = ''
    if (ser.inWaiting()):
        line = ser.read(1)
        print("line: " + str(line))
        s_line = split(line)
        #print("split: " + str(split(line)))
        s_line2 = []
        for i in s_line:
            s_line2.append(chr(i))
        print("split2: " + str(s_line2))
        #print("character: " + str(chr(i)))
        if (chr(i) == '|'):
            #print("data: " + str(data))
            if "End of timestep" in data:
                print("HELLLLOOO")
                flag = False
            elif "Failed to Detect Sensor at Position" not in data and "F" not in data and data != "":
                all_data.append(str.strip(data))
                print("all_data: " + str(all_data))
                data = ''
        else:
            data += chr(i)
            print("data: " + str(data))
    i += 1


print("all_data: " + str(all_data))
print("END")

'''coords1 = []
coords2 = []
temps = []

for i in all_data:
    values = i.split(",")
    coords1.append(values[0])
    coords2.append(values[1])
    temps.append(values[2])

print(coords1)
print(coords2)
print(temps)'''


ser.close()