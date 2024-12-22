# set recursion limit to 2001
import sys
sys.setrecursionlimit(999999)

with open(0) as file:
    content = file.read().strip()

MOD = 16777216

def simple_cal_secret(num):
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

def cal_secret(num, epochs, cache):
    if epochs == 0 or num == 0:
        return num

    if num in cache['1']:
        res =  cache['1'][num]
    else:
        res = num * 64
        res = res ^ num 
        res = res % MOD
        cache['1'][num] = res

    if res in cache['2']:
        res = cache['2'][res]
    else:
        res1 = res // 32
        res = res ^ res1
        res = res % MOD
        cache['2'][res] = res

    if res in cache['3']:
        res = cache['3'][res]
    else:
        res2 = res * 2048
        res = res ^ res2
        res = res % MOD
        cache['3'][res] = res

    return cal_secret(res, epochs - 1, cache)

nums = [int(i) for i in content.splitlines()]

total = 0

for i, num in enumerate(nums):
    print(str(i) + " out of " + str(len(nums)))
    res = num
    for _ in range(2000):
        res = simple_cal_secret(res)

    total += res

print(total)
