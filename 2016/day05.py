from hashlib import md5


def part1(doorid):
    index = 0
    password = ''
    while len(password) < 8:
        hash = md5(f'{doorid}{index}'.encode()).hexdigest()
        if hash[:5] == '00000':
            password += hash[5]
        index += 1
    return password


def part2(doorid):
    index = 0
    password = [None]*8
    count = 0
    while count < 8:
        hash = md5(f'{doorid}{index}'.encode()).hexdigest()
        if hash[:5] == '00000' and hash[5].isdigit():
            idx = int(hash[5])
            if idx < 8 and password[idx] is None:
                password[idx] = hash[6]
                count += 1
        index += 1
    return ''.join(password)
