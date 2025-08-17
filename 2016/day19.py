


def part1(raw_input):
    num_elves = int(raw_input.strip())
    elves = [[num,1] for num in range(1,num_elves+1)]
    while len(elves) > 1:
        new_elves = []
        for idx in range(len(elves)):
            taker = elves[idx]
            if idx<len(elves)-1:
                loser = elves[idx+1]
            else:
                loser = new_elves[0]
            if taker[1] > 0:
                new_elves.append([taker[0],taker[1]+loser[1]])
                loser[1] = 0
        elves = new_elves
    return elves[0][0]


def part2(raw_input):
    num_elves = int(raw_input.strip())
    elves = [[num,1] for num in range(1,num_elves+1)]
    idx1 = 0
    while len(elves) > 1:
        taker = elves[idx1]
        idx2 = idx1 + len(elves) // 2
        if idx2>=len(elves):
            idx2 = idx2 % len(elves)
        else:
            idx1 += 1
        loser = elves.pop(idx2)
        taker[1] += loser[1]
        if idx1 >= len(elves):
            idx1 = 0
    return elves[0][0]
