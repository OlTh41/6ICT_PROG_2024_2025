smiley = [
    [0, 1, 0, 1, 0],
    [0, 0, 2, 0, 0],
    [3, 0, 0, 0, 3],
    [0, 3, 3, 3, 0]
]

for i, list in enumerate(smiley):
    for j, num in enumerate(list):
        if num == 0:
            smiley[i][j] = " "
        elif num == 1:
            smiley[i][j] = "#"
        elif num == 2:
            smiley[i][j] = "."
        elif num == 3:
            smiley[i][j] = "-"

for i in range(len(smiley)):
    for j in range(len(smiley[i])):
        print(smiley[i][j], end="")
    print()  