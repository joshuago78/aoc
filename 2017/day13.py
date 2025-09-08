

def parse(raw_input):
    lines = raw_input.strip().split('\n')
    layers = []
    for line in lines:
        lyr, rng = line.split(': ')
        while len(layers) < int(lyr):
            layers.append(None)
        layers.append({
            'range': int(rng),
            'scanner_position': 0,
            'direction': 'down'
        })
    return layers


def advance(layer):
    if layer is not None:
        if layer['direction'] == 'down':
            if layer['scanner_position'] == layer['range']-1:
                layer['direction'] = 'up'
                return advance(layer)
            layer['scanner_position'] += 1
        else:
            if layer['scanner_position'] == 0:
                layer['direction'] = 'down'
                return advance(layer)
            layer['scanner_position'] -= 1


def part1(raw_input):
    layers = parse(raw_input)
    severity = 0
    for depth, layer in enumerate(layers):
        if layer and layer['scanner_position'] == 0:
            severity += depth * layer['range']
        for lyr in layers:
            advance(lyr)
    return severity


def part2(raw_input):
    layers = parse(raw_input)
    delay = 0
    while True:
        for i in range(len(layers)):
            scanner = layers[i]
            if scanner is not None:
                time = delay+i
                cycle = (scanner['range'] - 1) * 2
                if time % cycle == 0:
                    break
        else:
            return delay
        delay += 1
                

