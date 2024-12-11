from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn

with open(0) as file:
    content = file.read()

nums = [int(i) for i in content.split()]
epoch = 25

for e in range(epoch):
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Processing Epoch" + str(e) + "...", total=len(nums))
        new = []
        for num in nums:
            if num == 0:
                new.append(1)
            elif len(str(num)) % 2 == 0:
                mid = len(str(num)) // 2
                new.append(int(str(num)[:mid]))
                new.append(int(str(num)[mid:]))
            else:
                new.append(num * 2024)
            progress.advance(task)

    nums = new
    print("Epoch", e + 1)

print(nums)
print(len(nums))
