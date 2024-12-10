with open(0) as file:
    content = file.read().strip()

head = tuple()
dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

turns = {"^": ">", ">": "v", "v": "<", "<": "^"}


def print_grid(grid):
    for row in grid:
        print("".join(row))


grid = []
for i, line in enumerate(content.split("\n")):
    grid.append([])
    for j, c in enumerate(line):
        if c in dirs:
            head = (i, j)
        grid[i].append(c)

end = (len(grid) - 1, len(grid[0]) - 1)
curr = grid[head[0]][head[1]]

visited = set()
visited.add(head)

bounds = (len(grid)-1, len(grid[0])-1)

while True:
    x, y = head
    dx, dy = dirs[curr]
    nx, ny = x + dx, y + dy

    if not (0 <= nx <= bounds[0] and 0 <= ny <= bounds[1]):
        break

    if grid[nx][ny] == "#":
        curr = turns[curr]
    else:
        head = (nx, ny)
        visited.add(head)

print(len(visited))
