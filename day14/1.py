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


def predict_robo_pos(robo):
    x, y, vx, vy = robo
    t = 100

    a = (vx * t + x) % n
    b = (vy * t + y) % m

    return a, b


for robo in robots:
    x, y = predict_robo_pos(robo)
    pos.append((x, y))

for i in range(m):
    for j in range(n):
        if (j, i) in pos:
            print("#", end="")
        else:
            print(".", end="")
    print()

x_mid = n // 2  # 50
y_mid = m // 2  # 51

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for x, y in pos:
    if x < x_mid and y < y_mid:
        q1 += 1
    elif x < x_mid and y > y_mid:
        q2 += 1
    elif x > x_mid and y < y_mid:
        q3 += 1
    elif x > x_mid and y > y_mid:
        q4 += 1

print(q1 * q2 * q3 * q4)
