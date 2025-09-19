


def parse(raw_input):
    return [line.split(' => ') for line in raw_input.strip().split('\n')]


def split_image(image, div):
    tiles = []
    rstart = 0
    rstop = div
    while rstop<=len(image):
        cstart = 0
        cstop = div
        tilerow = []
        while cstop<=len(image):
            tilerow.append([image[r][cstart:cstop] for r in range(rstart,rstop)])
            cstart += div
            cstop += div
        tiles.append(tilerow)
        rstop += div
        rstart += div
    return tiles


def rotations(tile):
    r90 = [''.join([r[i] for r in tile][-1::-1]) for i in range(len(tile))]
    r180 = [''.join([r[i] for r in r90][-1::-1]) for i in range(len(tile))]
    r270 = [''.join([r[i] for r in r180][-1::-1]) for i in range(len(tile))]
    return [tile,r90,r180,r270]


def match_rule(rules, tile):
    for pattern, outbound in rules:
        if len(pattern.split('/')) == len(tile):
            for rotation in rotations(tile):
                if '/'.join(rotation) == pattern:
                    return outbound.split('/')
                # try flipping on y-axis
                elif '/'.join([l[-1::-1] for l in rotation]) == pattern:
                    return outbound.split('/')
                # try flipping on x-axis
                elif '/'.join(rotation[-1::-1]) == pattern:
                    return outbound.split('/')                    
    raise Exception('no match found')


def merge_tiles(tiles):
    image = []
    for tilerow in tiles:
        for row in range(len(tilerow[0])):
            image.append(''.join([tile[row] for tile in tilerow]))
    return image


def part1(raw_input, iterations=5):
    rules = parse(raw_input)
    image = ['.#.', '..#', '###']
    size = 3
    for i in range(iterations):
        div = 2 if size % 2 == 0 else 3
        tiles = split_image(image, div)
        new_tiles = []
        for r,tilerow in enumerate(tiles):
            new_tilerow = []
            for c,tile in enumerate(tilerow):
                inbound = '/'.join(tile)
                new_tilerow.append(match_rule(rules,tile))
            new_tiles.append(new_tilerow)
        image = merge_tiles(new_tiles)
        size = len(image)
    return ''.join(image).count('#')


def part2(raw_input):
    return part1(raw_input, iterations=18)

