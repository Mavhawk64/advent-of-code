# Day 6, Star 2
f = open("input.txt","r")
g = f.read()
# g = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
buf = [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
l = 1
n = 0
for i in g:
    buf[n] = i
    if buf[0] not in buf[1:] and buf[1] not in buf[2:] and buf[2] not in buf[3:] and buf[3] not in buf[4:] and buf[4] not in buf[5:] and buf[5] not in buf[6:] and buf[6] not in buf[7:] and buf[7] not in buf[8:] and buf[8] not in buf[9:] and buf[9] not in buf[10:] and buf[10] not in buf[11:] and buf[11] not in buf[12:] and buf[12] != buf[13] and None not in buf:
        break
    n = (n + 1) % 14
    l += 1
print(l,buf)