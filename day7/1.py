from itertools import product

with open(0) as f:
    lines = [l.strip() for l in f.readlines()]

total = 0

for line in lines:
    result, numbers = line.split(':')
    result = int(result)
    numbers = [int(i) for i in numbers.split()]

    n_op = len(numbers) - 1

    for operators in product('*+', repeat=n_op):
        op = iter(operators)
        res = numbers[0]
        for n in numbers[1:]:
            res = eval(f'{res}{next(op)}{n}')

        if res == result:
            total += result
            break
print(total)
