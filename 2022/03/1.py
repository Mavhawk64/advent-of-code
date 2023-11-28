# Day 3, Star 1

# Function that takes a char and returns a mapped value:
# a - z map to 1 - 26, A - Z map to 27 - 52 and that's it
def char_to_int(c):
    # a - z -> 1 - 26, A - Z -> 27 - 52
    if c.isalpha():
        return ord(c) - 38 if c.isupper() else ord(c) - 96
    # If it's not a letter, return 0
    return 0

f = open("input.txt", "r")
g = f.read().split('\n')
# Split each string in half
r = [[i[len(i)//2:], i[:len(i)//2]] for i in g]
# Get the only matching letter across each of the two strings
x = []
for i in r:
    # for each string pair, get the matching letter
    for j in i[0]:
        # if the letter is in the other string, print it
        if j in i[1]:
            x.append(j)
            break
# print(x)

# map each letter to a number using char_to_int
# then sum the numbers
print(sum([char_to_int(i) for i in x]))