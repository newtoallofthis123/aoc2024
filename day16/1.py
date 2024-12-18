from heapq import heappop, heappush

with open(0) as file:
    content = file.read().strip()

grid = []
end = ()
start = ()
dir = (0,1)

for i,line in enumerate(content.splitlines()):
    for j,c in enumerate(line):
        if c == 'S':
            start = (i,j)
        elif c == 'E':
            end = (i,j)
    grid.append(list(line))

# dikstra from start to end

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
turns = {
    (0,1): [(1,0),(-1,0)],
    (0,-1): [(1,0),(-1,0)],
    (1,0): [(0,1),(0,-1)],
    (-1,0): [(0,1),(0,-1)]
}

def is_bound(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    return True

visited = set()
pq = []
heappush(pq, (0, start, dir))

cost = {}
parent = {}
cost[(start, dir)] = 0

def reconstruct_path(parent, start, end, final_direction):
    path = []
    current = (end[0], end[1], final_direction)
    
    while current in parent:
        path.append((current[0], current[1]))
        current = parent[current]
    
    path.append(start) 
    path.reverse() 

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in path:
                print('X', end='')
            else:
                print(grid[i][j], end='')
        print()

    return len(path) - 1, path

while pq:
    curr_cost, pos, curr_dir = heappop(pq)

    if pos == end:
        print(reconstruct_path(parent, start, end, curr_dir))
        break

    if cost.get((pos, curr_dir), float('inf')) < curr_cost:
        continue

    dx,dy = curr_dir
    nx, ny = pos[0]+dx, pos[1]+dy

    if is_bound(nx, ny):
        if grid[nx][ny] != '#':
            if curr_cost + 1 < cost.get(((nx,ny), curr_dir), float('inf')):
                cost[((nx,ny), curr_dir)] = curr_cost + 1
                parent[(nx, ny, curr_dir)] = (pos[0], pos[1], curr_dir)
                heappush(pq, (curr_cost+1, (nx,ny), curr_dir))
        else:
            for t in turns[curr_dir]:
                if curr_cost + 1 < cost.get((pos, t), float('inf')):
                    cost[(pos, t)] = curr_cost + 1
                    parent[(pos[0], pos[1], t)] = (pos[0], pos[1], curr_dir)
                    heappush(pq, (curr_cost+1, pos, t))
