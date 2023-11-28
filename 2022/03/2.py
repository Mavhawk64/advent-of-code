# Day 3, Star 2
def char_to_int(c):
    # a - z -> 1 - 26, A - Z -> 27 - 52
    if c.isalpha():
        return ord(c) - 38 if c.isupper() else ord(c) - 96
    # If it's not a letter, return 0
    return 0

f = open("input.txt", "r")
# Split by every 3 lines
# abcdefg\nhijklm\nnopqrst\nuvwxyz\n1234567\n8901234 -> [[abcdefg, hijklm, nopqrst], [uvwxyz, 1234567, 8901234]]
g = f.read().split('\n')
g = [g[i:i+3] for i in range(0, len(g), 3)]
# Find the common letters in each set of 3
x = []
for i in g:
    # for each string pair, get the matching letter
    for j in i[0]:
        # if the letter is in the other string, print it
        if j in i[1] and j in i[2]:
            x.append(j)
            break

# map each letter to a number using char_to_int
# then sum the numbers
print(sum([char_to_int(i) for i in x]))