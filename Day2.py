with open("input2.txt") as f:
    a = f.readlines()

# part 1
h = 0
v = 0 
for i in range(len(a)):
    if a[i].split(' ')[0] == 'forward':
        h += int(a[i].split(' ')[1])
    elif a[i].split(' ')[0] == 'up':
        v -= int(a[i].split(' ')[1])
    else:
        v += int(a[i].split(' ')[1])

print(v*h)

# part 2
aim = 0
h = 0
d = 0
for i in range(len(a)):
    if a[i].split(' ')[0] == 'forward':
        h += int(a[i].split(' ')[1])
        d += aim * int(a[i].split(' ')[1])
    elif a[i].split(' ')[0] == 'up':
        aim -= int(a[i].split(' ')[1])
    else:
        aim += int(a[i].split(' ')[1])

print(d*h)
