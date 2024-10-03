filename = './data1.txt'

with open(filename, 'w') as f:
    for i in range(6000000):
        f.write('{}'.format(i))

