import json


def parse(raw_input):
    return json.loads(raw_input.strip())

'''
def count(data):
    if type(data) == int:
        return data
    total = 0
    if type(data) == dict:
        for key in data.keys():
            total += count(data[key])
    elif type(data) == list:
        for element in data:
            total += count(element)
    return total
'''

def count(data, no_red=False):
    if type(data) == int:
        return data
    total = 0
    if type(data) == dict:
        for key,value in data.items():
            if no_red and value == 'red':
                return 0
            total += count(data[key], no_red)
    elif type(data) == list:
        for element in data:
            total += count(element, no_red)
    return total


def part1(raw_input):
    data = parse(raw_input)
    return count(data)


def part2(raw_input):
    data = parse(raw_input)
    return count(data, no_red=True)
