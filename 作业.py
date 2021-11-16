x = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4,
     -0.30000000000000004, -0.19999999999999996, -0.09999999999999998,
     0.0, 0.10000000000000009, 0.19999999999999996, 0.30000000000000004,
     0.3999999999999999, 0.5, 0.6000000000000001, 0.7, 0.8,
     0.8999999999999999, 1.0]

y = [1.0, 0.78, 0.67, 0.51, 0.27, 0.0, 0.14, 0.19, -0.14, 0.03,
     0.03, -0.09, -0.03, -0.12, 0.14, 0.36, 0.57, 0.63, 0.61, 0.59, 1.01]
xy = []
length_x = len(x)
#print(length_x)
length_y = len(y)
#print(length_y)
if length_x > length_y :
    length = length_x
elif length_x < length_y:
    length = length_y
else:
    length = length_x
filename = "xy2.dat"
i = 0
with open("xy2.dat","w") as xy2:
    for i in range(length):
        xy.append(x.pop(0))
        xy.append(y.pop(0))
    for char in xy:
        i += 1
        if i >2 and i % 2 == 0:
            char = str(char) +'\n'
        else:
            char = str(char) +','
        xy2.write(char)
with open("xy2.dat","r") as infile:
    print(infile.readlines())
        