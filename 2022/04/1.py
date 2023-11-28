# Day 4, Star 1

def is_range_fully_contained(arr1,arr2):
    return arr1[0] >= arr2[0] and arr1[1] <= arr2[1]

f = open('input.txt', 'r')
g = f.read().split('\n')
# g is like ['1-3,5-7','2-7,5-10','20-99,90-95',...]
# Convert g to -> [[1,2,3],[5,6,7],[2,3,4,5,6,7],[20,21,22,...,99],[90,91,92,93,94,95],...]
# First split by comma, then split by dash, then convert to int
for i in g:
    # i is like '1-3,5-7'
    g[g.index(i)] = i.split(',')

# g is like [['1-3','5-7'],['2-7','5-10'],['20-99','90-95'],...]
# Convert g to -> [[[1,3],[5,7]], [[2,7],[5,10]], [[20,99],[90,95]],...]
g = [[[int(j) for j in i.split('-')] for i in j] for j in g]

# Define rfc to be an array of true or false depending on whether the range is fully contained for each pair in g
# This is determined by the function is_range_fully_contained
# rfc should be like [True,False,...]
# An example of a fully contained range is [1,3],[2,3] or [2,3],[1,3]
# An example of a non-fully contained range is [1,3],[2,4] or [2,4],[1,3]
rfc = [is_range_fully_contained(i[0],i[1]) or is_range_fully_contained(i[1],i[0]) for i in g]
print(rfc.count(True))
# print(rfc)