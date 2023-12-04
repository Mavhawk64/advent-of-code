# Day 2, Star 1
def do_work(sets, g_id):
    for set in sets:
        rolls = set.split(", ")
        for roll in rolls:
            amt = int(roll.split(" ")[0])
            color = roll.split(" ")[1]
            if color not in reqs or amt > reqs[color]:
                print("Game {} is invalid".format(g_id))
                return g_id
    return 0


with open("input.txt", "r") as f:
    id_sum = 5050
    reqs = {"red": 12, "green": 13, "blue": 14}
    g = f.read().split("\n")
    for game in g:
        g_id = int(game.split(":")[0][len("Game "):])
        print(g_id)
        sets = game.split(": ")[1].split("; ")
        id_sum -= do_work(sets, g_id)

    print(id_sum)
    f.close()
