with open(0) as file:
    content = file.read().strip()

robots = []

for line in content.splitlines():
    pos, v = line.split(" ")
    x, y = map(int, pos[2:].split(","))
    vx, vy = map(int, v[2:].split(","))

    robots.append((x, y, vx, vy))

n = 101
m = 103
pos = []
pos = [(r[0], r[1]) for r in robots]
vel = [(r[2], r[3]) for r in robots]
t = 0

while True:
    dist = set(pos)
    if len(dist) == len(pos):
        break

    for i in range(len(robots)):
        x, y = pos[i]
        vx, vy = vel[i]

        pos[i] = ((x + vx) % n, (y + vy) % m)
    t += 1

for i in range(m):
    for j in range(n):
        if (j, i) in pos:
            print("#", end="")
        else:
            print(".", end="")
    print()

print(t)
