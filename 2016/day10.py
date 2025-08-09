import re
from pprint import pprint


class Bin(object):

    def __init__(self, num):
        self.num = num
        self.value = None

    def __repr__(self):
        return f'<Bin {self.num}: value:{self.value}'

    def add_value(self, value):
        self.value = value


class Bot(object):

    def __init__(self, num):
        self.num = num
        self.values = []

    def __repr__(self):
        return f'<Bot {self.num}: values:{self.values}'

    def configure(self, high, low):
        self.high = high
        self.low = low

    def add_value(self, value):
        self.values.append(value)
        if len(self.values) == 2:
            self.give_out()

    def give_out(self):
        self.high.add_value(max(self.values))
        self.low.add_value(min(self.values))


def parse(raw_input):
    lines = raw_input.strip().split('\n')
    bots = [Bot(n) for n in range((len(lines)-raw_input.count('value')))]
    bins = [Bin(n) for n in range(raw_input.count('output'))]    
    bot_pattern = r'bot (?P<botnum>\d+) gives low to (?P<lowtype>bot|output) (?P<lownum>\d+) and high to (?P<hitype>bot|output) (?P<hinum>\d+)'
    value_pattern = r'value (?P<value>\d+) goes to bot (?P<botnum>\d+)'
    values = []
    for line in lines:
        if line.startswith('bot'):
            match = re.match(bot_pattern, line)
            d = match.groupdict()
            lowlist = bots if d['lowtype'] == 'bot' else bins
            low = lowlist[int(d['lownum'])]
            hilist = bots if d['hitype'] == 'bot' else bins
            hi = hilist[int(d['hinum'])]
            bots[int(d['botnum'])].configure(hi, low)
        else:
            match = re.match(value_pattern, line)
            value = (int(match.group('botnum')),int(match.group('value')))
            values.append(value)
    return bots, bins, values


def part1(raw_input):
    bots, bins, values = parse(raw_input)
    for bot,value in values:
        bots[bot].add_value(value)
    for bot in bots:
        if 61 in bot.values and 17 in bot.values:
            return bot.num


def part2(raw_input):
    bots, bins, values = parse(raw_input)
    for bot,value in values:
        bots[bot].add_value(value)
    return bins[0].value * bins[1].value * bins[2].value
