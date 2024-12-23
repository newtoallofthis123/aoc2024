# learnt from https://www.reddit.com/r/adventofcode/comments/1hkgj5b/comment/m3f1ziw

import sys
sys.setrecursionlimit(999999)

from collections import defaultdict

with open(0) as file:
    content = file.read().strip()

graph = defaultdict(set)
conns = set()

for line in content.splitlines():
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)
    conns.add(a)
    conns.add(b)



def bron_kerbosch(graph, r, p, x):
    def degree(node):
        return len(graph[node])

    if len(p) == 0 and len(x) == 0:
        yield r
    else:
        pivot = max(p | x, key=degree)
        for v in p - graph[pivot]:
            neighbours = graph[v]
            yield from bron_kerbosch(graph, r | {v}, p & neighbours, x & neighbours)
            p.remove(v)
            x.add(v)

clique = (bron_kerbosch(graph, set(), set(graph.keys()), set()))
clique = max(list(clique), key=len)
clique = sorted(clique)
print(','.join(clique))
