with open(0) as file:
    content = file.read().strip()

raw_grid, directions = content.split("\n\n")

dirs = {
    '>' : (0, 1),
    '<' : (0, -1),
    '^' : (-1, 0),
    'v' : (1, 0)
}
directions = [d for d in directions if d in dirs]

grid = []
robo = ()

for y, line in enumerate(raw_grid.split("\n")):
    row = []
    for x, char in enumerate(line):
        if char == "@":
            robo = (x, y)
        row.append(char)
    grid.append(row)

# print(grid, directions, robo)

def move(robo, direction):
    x, y = robo
    dx, dy = dirs[direction]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == "#":
        return robo
    if grid[nx][ny] == 'O':
        to_move = []
        while grid[nx][ny] == 'O':
            to_move.append((nx, ny))
            nx += dx
            ny += dy
        if grid[nx][ny] == '#':
            return robo
        to_move.reverse()
        for bx, by in to_move:
            grid[bx][by] = '.'
            grid[bx + dx][by + dy] = 'O'
        nx, ny = x + dx, y + dy
        grid[nx][ny] = '@'
        grid[x][y] = '.'
        return (nx, ny)

    grid[nx][ny] = '@'
    grid[x][y] = '.'
    return (nx, ny)

def print_grid():
    for row in grid:
        print("".join(row))

for dir in directions:
    robo = move(robo, dir)

def cal_gps(i, j):
    return 100 * i + j

total = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            total += cal_gps(i, j)

print(total)
print_grid()
