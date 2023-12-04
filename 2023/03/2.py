# Day 3, Star 2
import re
import numpy as np


def find_number(x, y, grid, numbs):
    the_number = ''
    if grid[x][y] not in numerals:
        return None
    z = y
    while z >= 0 and grid[x][z] in numerals:
        the_number = grid[x][z] + the_number
        z -= 1
    z = y+1
    while z <= len(grid[x])-1 and grid[x][z] in numerals:
        the_number = the_number + grid[x][z]
        z += 1
    return int(the_number)


with open("input.txt", "r") as f:
    numerals = list('0123456789')
    numbs = []
    g = f.read().split("\n")
    grid = [list(i) for i in g]
    for i in g:
        nums = re.split(r'\.|\+|\-|\#|\*|\@|\%|\=|\/|\$|\&', i)
        while '' in nums:
            nums.remove('')
        nums = [int(i) for i in nums]
        numbs.append(nums)
    s = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] in list('*'):
                # check up left, up, up right, left, right, down left, down, down right
                number = 0
                prevNumber = -1
                # up left
                if i > 0 and j > 0:
                    number = find_number(i-1, j-1, grid, numbs)
                    if number != None and number in numbs[i-1]:
                        numbs[i-1].remove(number)
                        prevNumber = number
                # up
                if i > 0:
                    number = find_number(i-1, j, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i-1]:
                        numbs[i-1].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number
                # up right
                if i > 0 and j < len(grid[i])-1:
                    number = find_number(i-1, j+1, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i-1]:
                        numbs[i-1].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number
                # left
                if j > 0:
                    number = find_number(i, j-1, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i]:
                        numbs[i].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number
                # right
                if j < len(grid[i])-1:
                    number = find_number(i, j+1, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i]:
                        numbs[i].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number
                # down left
                if i < len(grid)-1 and j > 0:
                    number = find_number(i+1, j-1, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i+1]:
                        numbs[i+1].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number
                # down
                if i < len(grid)-1:
                    number = find_number(i+1, j, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i+1]:
                        numbs[i+1].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number
                # down right
                if i < len(grid)-1 and j < len(grid[i])-1:
                    number = find_number(i+1, j+1, grid, numbs)
                    if number != None and prevNumber != number and number in numbs[i+1]:
                        numbs[i+1].remove(number)
                        if prevNumber != -1:
                            s += prevNumber * number
                        prevNumber = number

    print(s)
