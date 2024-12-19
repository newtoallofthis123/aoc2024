with open(0) as file:
    content = file.read().strip().split("\n\n")

patterns = {}
for p in content[0].split(', '):
    if len(p) == 1:
        patterns[p] = 9999
    else:
        patterns[p] = 1

desired = content[1].splitlines()

print(patterns, desired)

def is_possible(available, desired, dp={}):
    if dp is None:
        dp = {}
    if not desired:
        return True
    if desired in dp:
        return dp[desired]

    dp[desired] = False
    for i in range(1, len(desired) + 1):
        if desired[:i] in available and is_possible(available, desired[i:], dp):
            dp[desired] = True
            break

    return dp[desired]

total = 0
for d in desired:
    if is_possible(patterns, d):
        total += 1

print(total)
