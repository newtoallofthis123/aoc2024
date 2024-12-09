from collections import defaultdict
from itertools import permutations

with open(0) as file:
    content = file.read()

graph = [list(line) for line in content.split()]

n = len(graph)
m = len(graph[0])

def print_graph():
    for line in graph:
        print(''.join(line))
    print()

all_points = [(i, j) for i in range(n) for j in range(m)]

signals = defaultdict(list)

for i in range(n):
    for j in range(m):
        curr = graph[i][j]
        if curr == '.':
            continue
        else:
            signals[curr].append((i, j))

s = set()

def put_hashes(signal, points):
    possible = permutations(points, 2)
    for p in possible:
        x1, y1 = p[0]
        x2, y2 = p[1]
        px = 2*x1 - x2
        py = 2*y1 - y2
        if px < 0 or px >= n or py < 0 or py >= m:
            continue
        if graph[px][py] == '.':
            graph[px][py] = '#'
        if (px, py) not in s:
            s.add((px, py))
        qx = 2*x2 - x1
        qy = 2*y2 - y1
        if qx < 0 or qx >= n or qy < 0 or qy >= m:
            continue
        if graph[qx][qy] == '.':
            graph[qx][qy] = '#'
        if (qx, qy) not in s:
            s.add((qx, qy))

for signal in signals:
    put_hashes(signal, signals[signal])

print_graph()
print(len(s))
