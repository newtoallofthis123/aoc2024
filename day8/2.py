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

signals = defaultdict(list)

for i in range(n):
    for j in range(m):
        curr = graph[i][j]
        if curr == '.':
            continue
        else:
            signals[curr].append((i, j))

s = set()

def from_mid(a, b):
    x1, y1 = a
    x2, y2 = b
    px = 2*x1 - x2
    py = 2*y1 - y2
    if px >= 0 and px < n and py >= 0 and py < m:
        graph[px][py] = '#'
        return (px, py)
    else:
        return None


def put_hashes(points):
    possible = permutations(points, 2)
    for p in possible:
        a, b = p
        left = (a, b)
        right = (a, b)

        while left:
            if p := from_mid(*left):
                left = (p, a)
                s.add(p)
            else:
                break

        while right:
            if p := from_mid(*right):
                right = (b, p)
                s.add(p)
            else:
                break

        s.add(a)
        s.add(b)

for signal in signals:
    put_hashes(signals[signal])

print_graph()
print(len(s))
