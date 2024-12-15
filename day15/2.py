# Doesn't work

with open(0) as file:
    content = file.read().strip()

raw_grid, directions = content.split("\n\n")

dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
directions = [d for d in directions if d in dirs]

grid = []
robo = ()

for y, line in enumerate(raw_grid.split("\n")):
    row = []
    for x, char in enumerate(line):
        if char == "@":
            char = "@."
        if char == "O":
            char = "[]"
        if char == "#":
            char = "##"
        if char == ".":
            char = ".."
        row.append(char[0])
        row.append(char[1])
    grid.append(row)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            robo = (i, j)

print(grid, directions, robo)


def discover_packs(pos, dir):
    px, py = pos
    dx, dy = dirs[dir]
    packs = set()
    queue = [(px + dx, py + dy)]
    while queue:
        x, y = queue.pop(0)
        if grid[x][y] in "[]":
            queue.append((x + dx, y + dy))

    return packs


def move(robo, direction):
    x, y = robo
    dx, dy = dirs[direction]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == "#":
        return robo

    grid[nx][ny] = "@"
    grid[x][y] = "."
    return (nx, ny)


def print_grid():
    for row in grid:
        print("".join(row))


for dir in ["<", "v", "v", "<", "<", "^"]:
    print("Moving", dir)
    robo = move(robo, dir)
    print_grid()

# def cal_gps(i, j):
#     return 100 * i + j
#
# total = 0
#
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 'O':
#             total += cal_gps(i, j)

# print(total)
# print_grid()
