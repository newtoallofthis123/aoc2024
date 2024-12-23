from collections import defaultdict

with open(0) as file:
    content = file.read().strip()

graph = defaultdict(list)

for line in content.splitlines():
    a, b = line.split('-')
    graph[a].append(b)
    graph[b].append(a)

from itertools import combinations

def find_conn(graph, node):
    possi = combinations(graph[node], 2)
    res = []
    for p in possi:
        if p[1] in graph[p[0]] and p[0] in graph[p[1]]:
            res.append((node, p[0], p[1]))

    return res

res = []
for g in graph:
    res += find_conn(graph, g)

res = set(map(lambda x: tuple(sorted(x)), res))
res = sorted(res)

def ret_t(res):
    t = set()
    for r in res:
        for i in r:
            if i.startswith('t'):
                t.add(r)
                break
    return t

res = ret_t(res)
print('\n'.join(map(str, res)))
print(len(res))
