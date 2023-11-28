# Day 2, Star 1

# A, X -> Rock
# B, Y -> Paper
# C, Z -> Scissors
a = ['A', 'B', 'C']
b = ['X', 'Y', 'Z']
# X = 1, Y = 2, Z = 3, Loss = 0, Draw = 3, Win = 6
f = open("input.txt", "r")
g = f.read().split('\n')
r = [i.split(' ') for i in g]

combos = {}
[combos.update({r[i][0] + r[i][1]: combos.get(r[i][0] + r[i][1], 0) + 1}) for i in range(0,len(r))]
# print(combos)

# Win is classified as b[(i+1)%3] == a[i]
# Loss is classified as b[(i-1)%3] == a[i]
# Draw is classified as b[i] == a[i]

points = 0
for i in combos:
    if a.index(i[0]) == b.index(i[1]):
        points += 3*combos[i]
    elif b[(a.index(i[0])+1)%3] == i[1]:
        points += 6*combos[i]
    
    # Add the points based on X, Y, Z
    points += combos[i]*(b.index(i[1])+1)
print(points)

f.close()