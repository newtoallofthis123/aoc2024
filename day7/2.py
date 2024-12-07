from itertools import product
from functools import reduce
from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn

with open(0) as f:
    lines = [l.strip() for l in f.readlines()]

total = 0

def operate(x, y, op):
    if op == '*':
        return x * y
    elif op == '+':
        return x + y

    return int(str(x) + str(y))

visited = set()

def normal_solve(line):
    total = 0
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
            visited.add(line)
            break

    return total

def join_solve(line):
    total = 0
    result, numbers = line.split(':')
    result = int(result)
    numbers = [int(i) for i in numbers.split()]

    n_op = len(numbers) - 1

    for operators in product('*+|', repeat=n_op):
        op = iter(operators)
        tot = reduce(lambda x, y: operate(x,y, next(op)), numbers)

        if tot == result:
            total += result
            visited.add(line)
            break

    return total

with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Processing...", total=len(lines)*2)
        for line in lines:
            total += normal_solve(line)
            progress.update(task, advance=1)

        for line in lines:
            if line not in visited:
                total += join_solve(line)
            progress.update(task, advance=1)

print(total)
