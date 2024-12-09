with open(0) as file:
    content = file.read().strip()

content = [int(i) for i in content]

arr = []

i = 0
c = 0
while i < len(content):
    block_size = content[i]
    free_size = 0
    if i + 1 < len(content):
        free_size = content[i+1]

    for _ in range(block_size):
        arr.append(c)
    c += 1
    for _ in range(free_size):
        arr.append(-1)

    i += 2

print(arr)

i = 0
j = len(arr) - 1 

while i != j:
    if arr[i] == -1 and arr[j] != -1:
        arr[i], arr[j] = arr[j], arr[i]
    if arr[i] != -1:
        i += 1
    if arr[j] == -1:
        j -= 1

total = 0
print(arr)

for i, c in enumerate(arr):
    if c != -1:
        total += i*c 

print(total)
