from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn

from functools import cache


with open(0) as file:
    content = file.read()

nums = [int(i) for i in content.split()]
epoch = 75

@cache
def count_stones(stone: int, steps: int) -> int:
    if steps == 0:
        return 1
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        first = int(str_stone[:mid])
        second = int(str_stone[mid:])
        return count_stones(first, steps - 1) + count_stones(second, steps - 1)
    else:
        next_stone = stone * 2024 if stone != 0 else 1
        return count_stones(next_stone, steps - 1)

total = 0

with Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TimeElapsedColumn(),
    transient=True,
) as progress:
    task = progress.add_task("[cyan]Processing Epoch...", total=len(nums))
    for num in nums:
        total += count_stones(num, epoch)
        progress.advance(task)

print(total)
