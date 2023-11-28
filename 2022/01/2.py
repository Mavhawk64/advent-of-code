# Day 1, Star 2
f = open("input.txt", "r")
g = f.read().split('\n\n')
a = [sum([int(x) for x in i.split('\n')]) for i in g]
a.sort()
print(a[-1] + a[-2] + a[-3])
f.close()
