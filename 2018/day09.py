from collections import deque
import re


def parse(text):
    p = r'(?P<plyrs>\d+) players; last marble is worth (?P<mrbls>\d+) points'
    m = re.match(p, text)
    return int(m.group('plyrs')), int(m.group('mrbls'))+1


def part1(text, multiplier=1):
    player_count, marble_count = parse(text)
    marble_count *= multiplier
    scores = [0 for _ in range(player_count)]
    circle = deque([0,1])
    for marble in range(2,marble_count):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % player_count] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return max(scores)


def part2(text):
    return part1(text, multiplier=100)
    