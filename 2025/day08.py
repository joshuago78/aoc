from math import sqrt

MAX_CONNECTIONS = 1000


class Circuit(object):

    def __init__(self, box):
        self.boxes = [box,]

    def __repr__(self):
        return f'<Circuit {self.id} size:{len(self.boxes)}>'


class Box(object):

    def __init__(self, id, triple):
        self.id = id
        self.triple = [int(num) for num in triple.split(',')]
        self.connected = []
        self.circuit = Circuit(self)

    def __repr__(self):
        return f'<Box {self.id}: {','.join([str(n) for n in self.triple])}>'

    def distance(self, box2):
        (x1,y1,z1),(x2,y2,z2) = self.triple, box2.triple
        return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    def connect_to(self, box2):
        self.connected.append(box2)
        box2.connected.append(self)
        if box2 not in self.circuit.boxes:
            old_circuit = box2.circuit
            self.circuit.boxes.extend(box2.circuit.boxes)
            for box in box2.circuit.boxes:
                box.circuit = self.circuit
            return old_circuit


def parse(data):
    boxes = []
    for id, triple in enumerate(data.strip().split('\n')):
        box = Box(id, triple)
        boxes.append(box)
    return boxes


def get_all_distances(boxes):
    distances = []
    for box1 in boxes:
        for box2 in boxes:
            if box1 != box2:
                distances.append((box1.distance(box2),box1,box2))
    distances.sort(key=lambda x: x[0])
    return distances


def part1(data):
    boxes = parse(data)
    distances = get_all_distances(boxes)
    connections = 0
    while connections < MAX_CONNECTIONS:
        _,box1,box2 = distances.pop(0)
        if box2 not in box1.connected:
            box1.connect_to(box2)
            connections += 1
    circuits = sorted(set(b.circuit for b in boxes), key=lambda c: len(c.boxes), reverse=True)
    return len(circuits[0].boxes) * len(circuits[1].boxes) * len(circuits[2].boxes)


def part2(data):
    boxes = parse(data)
    circuits = [b.circuit for b in boxes]
    distances = get_all_distances(boxes)
    connections = 0
    while len(circuits) > 1:
        _,box1,box2 = distances.pop(0)
        if box2 not in box1.connected:
            old_circuit = box1.connect_to(box2)
            connections += 1
            if old_circuit:
                circuits.pop(circuits.index(old_circuit))
    return box1.triple[0] * box2.triple[0]
