# Day 5, Star 2
# Day 5, Star 1
def parse_line(s):
    # move x from a to b
    x = int(s.split('move ')[1].split(' from ')[0])
    a = int(s.split(' from ')[1].split(' to ')[0])
    b = int(s.split(' from ')[1].split(' to ')[1])
    return x, a, b

def apply_move(x,a,b,blx):
    movers = blx[a][-x:]
    blx[a] = blx[a][:-x]
    for i in range(len(movers)):
        blx[b].append(movers[i])
    # print(blx[b],blx)
    return blx

f = open("input.txt","r")
g = f.read().split('\n\n')[1].split('\n')
g = [parse_line(s) for s in g]
blocks = {1: ["W","B","D","N","C","F","J"], 2: ["P","Z","V","Q","L","S","T"], 3: ["P","Z","B","G","J","T"], 4: ["D","T","L","J","Z","B","H","C"], 5: ["G","V","B","J","S"], 6: ["P","S","Q"], 7: ["B","V","D","F","L","M","P","N"], 8: ["P","S","M","F","B","D","L","R"], 9: ["V","D","T","R"]}
# blocks = {1: ["Z","N"], 2: ["M","C","D"],3: ["P"]}
# print(g[0])
for i in range(0,len(g)):
    blocks = apply_move(g[i][0],g[i][1],g[i][2],blx=blocks)
# print(blocks)

for i in blocks:
    print(blocks[i][-1],end='')
print()