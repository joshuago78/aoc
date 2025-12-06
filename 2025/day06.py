

def parse(data):
    lines = data.split('\n')
    splits = [i for i in range(len(lines[0])) if not any([line[i].strip() for line in lines])]
    splits.append(len(lines[0]))
    problems = []
    start = 0
    for split in splits:
        operand = lines[-1][start:split]
        numbers = [line[start:split] for line in lines[:-1]]
        problems.append((operand,numbers))
        start = split+1
    return problems


def rewrite_numbers(problems):
    new_problems = []
    for op,nums in problems:
        new_nums = []
        for d in range(len(nums[0])):
            new_nums.append(''.join([num[d] for num in nums]))
        new_problems.append((op, new_nums))
    return new_problems


def part1(data, part2=False):
    problems = parse(data)
    if part2:
        problems = rewrite_numbers(problems)
    total = 0
    for op, nums in problems:
        total += eval(op.join(nums))
    return total


def part2(data):
    return part1(data, part2=True)
