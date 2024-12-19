from heapq import heappop, heappush

with open(0) as file:
    content = file.read().strip()

grid = []
end = ()
start = ()

for i,line in enumerate(content.splitlines()):
    for j,c in enumerate(line):
        if c == 'S':
            start = (i,j)
        elif c == 'E':
            end = (i,j)
    grid.append(list(line))

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dikjstra(grid, start, end):
    queue = [(0, start[0], start[1], 0)]
    visited = set()

    while queue:
        cost, x, y, d = heappop(queue)

        if (x, y) == end:
            return cost

        if (x, y, d) in visited:
            continue
        visited.add((x, y, d))

        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
            heappush(queue, (cost + 1, nx, ny, d))

        for nd in [(d - 1) % 4, (d + 1) % 4]:
            heappush(queue, (cost + 1000, x, y, nd))

print(start, end)
print(dikjstra(grid, start, end))
