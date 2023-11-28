# Day 1, Star 1
print(max([sum([int(x) for x in i.split('\n')]) for i in open('input.txt', 'r').read().split('\n\n')]))