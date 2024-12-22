with open(0) as file:
    content = file.read().strip()

MOD = 16777216

def cal_secret(num):
    res = num * 64
    res = res ^ num 
    res = res % MOD

    res1 = res // 32
    res = res ^ res1
    res = res % MOD

    res2 = res * 2048
    res = res ^ res2
    res = res % MOD

    return res

nums = [int(i) for i in content.splitlines()]

cache = {}
for num in nums:
    last = num % 10
    diffs = []
    for _ in range(2000):
        num = cal_secret(num)
        temp = num % 10
        diffs.append((temp - last, temp))
        last = temp
    seen = set()
    for i in range(2000-4):
        part = (diffs[i][0], diffs[i+1][0], diffs[i+2][0], diffs[i+3][0])
        val = diffs[i+3][1]
        if part not in seen:
            seen.add(part)
            if part not in cache:
                cache[part] = val
            else:
                cache[part] += val
ret = 0
for val in cache.values():
    ret = max(ret, val)

print(ret)
