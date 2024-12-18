with open(0) as file:
    content = file.read().strip()

raw_pos = [list(map(int, line.split(","))) for line in content.splitlines()]

n = 70
m = 70

pos = raw_pos[:1024]

grid = [["." for _ in range(m + 1)] for _ in range(n + 1)]
for x, y in pos:
    grid[y][x] = "#"

target = (n, m)

import heapq


def dijkstra(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))
    distances = {(start[0], start[1]): 0}
    visited = set()

    while pq:
        dist, x, y = heapq.heappop(pq)

        if (x, y) == goal:
            return dist

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n + 1 and 0 <= ny < m + 1 and grid[nx][ny] == ".":
                new_dist = dist + 1
                if new_dist < distances.get((nx, ny), float("inf")):
                    distances[(nx, ny)] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    return -1

for p in raw_pos[1024:]:
    x, y = p
    grid[y][x] = "#"
    print("Trying", x, y)
    if dijkstra(grid, (0, 0), target) == -1:
        print(x, y)
        break
