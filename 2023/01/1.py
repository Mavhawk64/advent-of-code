# Day 1, Star 1

def parse_int(s):
    dec = 0
    x = 0
    for i in range(1, len(s)+1):
        print(s[-i], s[-i] in ['1', '2', '3', '4',
              '5', '6', '7', '8', '9', '0'], x, dec)
        if s[-i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            x += 10**dec * int(s[-i])
            dec += 1
            break

    for i in range(0, len(s)):
        if s[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            x += 10**dec * int(s[i])
            break
    print(x)
    return x


with open("input.txt") as f:
    g = f.read().split('\n')
    s = 0
    for i in g:
        s += parse_int(i)
    print(s)
    f.close()
