with open("input3.txt") as f:
    a = [x for x in f.read().split()]


# part 1
gamma = ''
epsilon = ''
for i in range(len(a[0])):
    zero = 0
    one = 0
    for j in range(len(a)):
        if a[j][i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

g = int(gamma,2)
e = int(epsilon, 2)
print(g*e)

# part 2
# calculating oxygen
data = a
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for i in range(len(data)):
        if data[i][index] == '1':
            one += 1
            ones.append(data[i])
        else:
            zero += 1
            zeroes.append(data[i])
    if zero > one:
        data = zeroes
    else:
        data = ones
    index += 1

ox = int(data[0], 2)

# calculating co2
data = a
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for i in range(len(data)):
        if data[i][index] == '1':
            one += 1
            ones.append(data[i])
        else:
            zero += 1
            zeroes.append(data[i])
    if zero > one:
        data = ones
    else:
        data = zeroes
    index += 1

co2 = int(data[0], 2)
print(ox*co2)
