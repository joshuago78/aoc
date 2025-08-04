

def find_primes(target):
    target = target // 10
    primes = [2,]
    total = 3
    for i in range(3,target+1):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
            total += i
    return primes


def how_many_gifts(primes, house, verbose=False):
    elves = set([1,])
    for prime in primes:
        if prime > house:
            break
        if house % prime == 0:
            elf = prime
            while elf <= house:
                if house % elf == 0:
                    elves.add(elf)
                elf += prime
    gifts = 11 * sum(elves)
    if verbose:
        print(f'House {house} visted by elves {sorted(elves)} got {gifts} gifts.')
    return gifts


def part1(raw_input):
    target = int(raw_input)
    stop = target//10
    houses = [0]*(stop)
    for elf in range(1,stop):
        for house in range(elf,stop,elf):
            houses[house] += elf * 10
    for house,gifts in enumerate(houses):
        if gifts >= target:
            return house



def part2(raw_input):
    target = int(raw_input)
    stop = target//10
    houses = [0]*(stop)
    elves = [0]*(stop)
    for elf in range(1,stop):
        for house in range(elf,stop,elf):
            if elves[elf] < 50:
                houses[house] += elf * 11
                elves[elf] += 1
    for house,gifts in enumerate(houses):
        if gifts >= target:
            return house

