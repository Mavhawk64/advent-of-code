# Day 1, Star 2
def parse_int(s):
    alphabet = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    word = ''
    words = []
    i = 0
    while i < len(s):
        word += s[i]
        # print(i, word)
        if len([j for j in alphabet if j.startswith(word)]) == 0:
            i -= len(word) - 1
            # print(word, i, s[i], "not in alphabet")
            word = ''
        if s[i] in alphabet or word in alphabet:
            words.append(word)
            i -= len(word) - 1
            word = ''
        i += 1
    print(words)
    return 10*(alphabet.index(words[0]) % 10) + (alphabet.index(words[-1]) % 10)


with open("input.txt") as f:
    g = f.read().split('\n')
    s = 0
    for i in g:
        # print(i)
        s += parse_int(i)
    print(s)
    f.close()
