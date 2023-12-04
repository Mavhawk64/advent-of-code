# Day 2, Star 2
def do_work(sets, g_id):
    min_colors = {}
    for set in sets:
        rolls = set.split(", ")
        for roll in rolls:
            amt = int(roll.split(" ")[0])
            color = roll.split(" ")[1]
            if color not in min_colors or amt > min_colors[color]:
                min_colors[color] = amt
    print(min_colors)
    return min_colors["red"] * min_colors["green"] * min_colors["blue"]


with open("input.txt", "r") as f:
    g = f.read().split("\n")
    power_sum = 0
    for game in g:
        g_id = int(game.split(":")[0][len("Game "):])
        print(g_id)
        sets = game.split(": ")[1].split("; ")
        power_sum += do_work(sets, g_id)
    print(power_sum)
    f.close()
