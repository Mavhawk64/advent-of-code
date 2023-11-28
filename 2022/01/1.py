# Day 1, Star 1
f = open('input.txt', 'r')
g = f.read().split('\n\n')
print(max([sum([int(x) for x in i.split('\n')]) for i in g]))
f.close()