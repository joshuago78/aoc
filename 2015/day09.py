import re
from copy import deepcopy


def parse(raw_input):
    cities = {}
    for line in raw_input.strip().split('\n'):
        match = re.match(r'(?P<a>\w+) to (?P<b>\w+) = (?P<dist>\d+)', line)
        a = match.group('a')
        b = match.group('b')
        dist = int(match.group('dist'))
        if a not in cities.keys():
            cities[a] = {}
        cities[a][b] = dist
        if b not in cities.keys():
            cities[b] = {}
        cities[b][a] = dist
    return cities


def shortest(cities, city, visited, distance):
    best = None
    neighbors = [n for n in cities[city].keys() if n not in visited]
    if len(neighbors) == 0:
        print(f'path: {visited}, distance: {distance}')
        return distance, deepcopy(visited)
    for neighbor in neighbors:
        d_to_n = cities[city][neighbor]
        visited.append(neighbor)
        new_d, path = shortest(cities, neighbor, visited, distance + d_to_n)
        if best is None or new_d < best:
            best = new_d
            best_path = path
        visited.pop()
    return best, best_path


def longest(cities, city, visited, distance):
    best = None
    neighbors = [n for n in cities[city].keys() if n not in visited]
    if len(neighbors) == 0:
        print(f'path: {visited}, distance: {distance}')
        return distance, deepcopy(visited)
    for neighbor in neighbors:
        d_to_n = cities[city][neighbor]
        visited.append(neighbor)
        new_d, path = longest(cities, neighbor, visited, distance + d_to_n)
        if best is None or new_d > best:
            best = new_d
            best_path = path
        visited.pop()
    return best, best_path


def part1(raw_input):
    cities = parse(raw_input)
    best = None
    best_path = None
    for city in cities.keys():
        visited = [city,]
        dist, path = shortest(cities, city, visited, 0)
        if best is None or dist < best:
            best = dist
            best_path = path
    print(f'best path = {best_path}: {best}')
    return best


def part2(raw_input):
    cities = parse(raw_input)
    best = None
    best_path = None
    for city in cities.keys():
        visited = [city,]
        dist, path = longest(cities, city, visited, 0)
        if best is None or dist > best:
            best = dist
            best_path = path
    print(f'best path = {best_path}: {best}')
    return best
