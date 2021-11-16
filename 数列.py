# (-5,5)
a = list(range(-50,51,1))
for i in range(len(a)):
    a[i] = a[i]/10
#print(a)
b = []
for num in a:
    num = num ** 3
    b.append(num)
#print(b)

with open('pow3.csv','w') as pow3:
    ab = zip(a,b)
    print(ab)
    for i in ab:
        char = '{0},{1}\n'.format(i[0],i[1])
        pow3.write(char)

with open('pow3.csv','r') as infile:
    print(infile.readlines())