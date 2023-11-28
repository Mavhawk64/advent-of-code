# Day 2, Star 2

f = open("input.txt", "r")
g = f.read().split('\n')
r = [i.split(' ') for i in g]

a = ['A', 'B', 'C']
b = ['X', 'Y', 'Z']

# X = 0, Y = 3, Z = 6
combos = {}
[combos.update({r[i][0] + r[i][1]: combos.get(r[i][0] + r[i][1], 0) + 1}) for i in range(0,len(r))]
points = 0
for i in combos:
    # Add the points based on X, Y, Z
    points += combos[i]*(3 * b.index(i[1]))
    # I guarantee there is a better way to do this, but I'm tired
    # if X -> a.index(a[(a.index(i[0]) - 1) % 3]) + 1
    # if Y -> a.index(i[0]) + 1
    # if Z -> a.index(a[(a.index(i[0]) + 1) % 3]) + 1
    if i[1] == 'X':
        points += combos[i]*(a.index(a[(a.index(i[0]) - 1) % 3]) + 1)
    elif i[1] == 'Y':
        points += combos[i]*(a.index(i[0]) + 1)
    elif i[1] == 'Z':
        points += combos[i]*(a.index(a[(a.index(i[0]) + 1) % 3]) + 1)
print(points)