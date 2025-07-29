


def increment(password):
    password = list(password)
    for i in range(len(password)-1,-1,-1):
        if password[i] == 'z':
            password[i] = 'a'
            continue
        password[i] = chr(ord(password[i])+1)
        return ''.join(password)


def has_straight(password):
    for i in range(len(password)-3):
        a,b,c = password[i:i+3]
        if ord(b) - ord(a) == 1 and ord(c) - ord(b) == 1:
            return True
    return False


def has_no_iol(password):
    return 'i' not in password and \
        'o' not in password and \
        'l' not in password


def has_two_pairs(password):
    one_pair = False
    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            if one_pair == True:
                return True
            one_pair = True
            i += 1
        i += 1
    return False


def valid(password):
    return has_straight(password) and \
        has_no_iol(password) and \
        has_two_pairs(password)


def part1(raw_input):
    password = increment(raw_input)
    while not valid(password):
        password = increment(password)
    return password


def part2(raw_input):
    pass
