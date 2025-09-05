from functools import reduce


SIZE = 256
#SIZE = 16


def print_nums(nums, start, stop):
    output = ''
    for index, num in enumerate(nums):
        if index == start:
            output += f'([{num}]'
        else:
            output += str(num)
        if index == stop - 1 or (stop==0 and index==len(nums)-1):
            output += ')'
        if index < len(nums) - 1:
            output += ' '
    print(output)


def sparse_hash(nums, lengths, start=0, skip_size=0):
    for length in lengths:
        stop = (start+length) % SIZE
        if length > 0:
            if stop > start:
                nums = nums[:start] + list(reversed(nums[start:stop])) + nums[stop:]
            else:
                subset = list(reversed(nums[start:] + nums[:stop]))
                subsplit = SIZE - start
                nums = subset[subsplit:] + nums[stop:start] + subset[:subsplit]
        start = (stop + skip_size) % SIZE
        skip_size += 1
    return nums, start, skip_size


def part1(raw_input):
    lengths = [int(i) for i in raw_input.strip().split(',')]
    nums = list(range(SIZE))
    nums, _, _ = sparse_hash(nums, lengths)
    return nums[0]*nums[1]


def part2(raw_input):
    lengths = [ord(c) for c in raw_input.strip()] + [17, 31, 73, 47, 23]
    nums = list(range(SIZE))
    start, skip_size = 0, 0
    for _ in range(64):
        nums, start, skip_size = sparse_hash(nums, lengths, start, skip_size)
    dense_hash = ''
    for i in range(16):
        chunk = nums[i*16:i*16+16]
        dense_hash += f'{reduce(lambda x,y: x^y, chunk):x}'
    return dense_hash





