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

j = len(arr) - 1 
prev = arr[j]
j -= 1

blocks = []
block = [(j+1, prev)]
while j >= 0:
    if arr[j] == prev and arr[j] != -1:
        block.append((j, prev))
    elif arr[j] != prev and arr[j] != -1:
        blocks.append(block)
        block = [(j, arr[j])]
        prev = arr[j]

    j -= 1

def print_block(arr):
    for b in arr:
        if b == -1:
            print('.', end='')
        else:
            print(b, end='')
    print()

for block in blocks:
    i = 0
    free_block = []
    in_free = False
    while i < len(arr):
        if arr[i] == -1:
            free_block.append(i)
            in_free = True
        elif arr[i] != -1 and in_free:
            if len(free_block) >= len(block):
                break
            else:
                free_block = []
                in_free = False
        i += 1

    if len(free_block) >= len(block) and sum([b[0] for b in block]) > sum(free_block[:len(block)]):
        for i,b in enumerate(block):
            # print(b)
            arr[b[0]] = -1
            arr[free_block[i]] = b[1]
        # print_block(arr)

total = 0
print(arr)

for i, c in enumerate(arr):
    if c != -1:
        total += i*c 

print(total)
