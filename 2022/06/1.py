# Day 6, Star 1
f = open("input.txt","r")
g = f.read()
buf = [None,None,None,None]
l = 1
n = 0
for i in g:
    buf[n] = i
    if buf[0] != buf[1] and buf[0] != buf[2] and buf[0] != buf[3] and buf[1] != buf[2] and buf[1] != buf[3] and buf[2] != buf[3] and None not in buf:
        break
    n = (n + 1) % 4
    l += 1
print(l,buf)
print(g.index('nhwd'))
print(g[1352])