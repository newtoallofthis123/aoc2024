with open(0) as file:
    content = file.read().strip()

heads = []
lines = []
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i,line in enumerate(content.split('\n')):
    lines.append([])
    for j,c in enumerate(line):
        if c == '0':
            heads.append((i, j))
        lines[i].append(int(c))

print(lines)
print(heads)

head = heads[0]
total = 0
for head in heads:
    queue = [head]
    found = set()
    while queue:
        x, y = queue.pop(0)
        print(x, y)
        if lines[x][y] == 9:
            found.add((x, y))
            print('Found 9 at', x, y)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]) and lines[nx][ny] != 0:
                if lines[nx][ny] - lines[x][y] == 1:
                    queue.append((nx, ny))
    total += len(found)

print(total)
