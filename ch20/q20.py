import sys

data = open(sys.argv[1]).read().strip().split('\n\n')

class Tile:
    def __init__(self, id, data, rotation=0, flip_x=False, flip_y=False):
        self.id = id
        self.data = self.modify(data, rotation, flip_x, flip_y)
        self.borders = self.get_borders()

        self.rotation = rotation
        self.flip_x = flip_x
        self.flip_y = flip_y

    def modify(self, data, rotation, flip_x, flip_y):
        d = data

        for _ in range(rotation):
            d = list(zip(*reversed(d)))
        d = [''.join(x) for x in d]

        if (flip_x):
            d = [x[::-1] for x in d]

        if (flip_y):
            d = d[::-1]

        return d

    def get_borders(self):
        b = []
        b.append(self.data[0]) #top
        b.append(''.join([x[-1] for x in self.data])) #right
        b.append(self.data[-1]) #bottom
        b.append(''.join([x[0] for x in self.data])) #left
        return b

    def __str__(self):
        return 'Tile ID: %s' % (self.id,)

    def __repr__(self):
        return 'Tile ID: %s' % (self.id,)

tiles = {}
for tile in data:
    tile = tile.split('\n')
    tile_id = tile[0][5:-1]
    tiles[tile_id] = Tile(tile_id, tile[1:])

correct_tiles = {}
correct_borders = {}
tile_ids = list(tiles.keys())
first_tile = tile_ids[0]
correct_tiles[(0,0)] = tiles[first_tile]
correct_borders[(0,0)] = tiles[first_tile].borders
del tiles[first_tile]

def check_tile(new_tile):
    for pos in correct_borders:
        borders = correct_borders[pos]
        for border in new_tile.borders:
            if (border not in borders):
                continue
            direction = borders.index(border)

            new_pos = pos
            if (direction == 0):
                new_pos = (new_pos[0],new_pos[1]-1)
            elif (direction == 1):
                new_pos = (new_pos[0]+1,new_pos[1])
            elif (direction == 2):
                new_pos = (new_pos[0],new_pos[1]+1)
            elif (direction == 3):
                new_pos = (new_pos[0]-1,new_pos[1])

            up    = (new_pos[0], new_pos[1]-1)
            right = (new_pos[0]+1, new_pos[1])
            down  = (new_pos[0], new_pos[1]+1)
            left  = (new_pos[0]-1, new_pos[1])

            valid_pairs = []
            for i,direction_pos in enumerate([up, right, down, left]):
                if (not direction_pos in correct_borders):
                    continue
                if (new_tile.borders[i] != correct_borders[direction_pos][(i+2)%4]):
                    break
                valid_pairs.append((i,direction_pos))
            else:
                correct_borders[new_pos] = new_tile.borders
                for i,x in valid_pairs:
                    correct_borders[x][(i+2)%4] = None
                    correct_borders[new_pos][i] = None
                return new_pos
    return -1

cache_tiles = {}
def check_all_variations(tile):
    for rotation in range(4):
        for flip_x in range(2):
            for flip_y in range(2):
                a = (tile.id, rotation, flip_x, flip_y)
                if (a in cache_tiles):
                    new_tile = cache_tiles[a]
                else:
                    new_tile = Tile(tile.id, tile.data, rotation, flip_x, flip_y)
                    cache_tiles[a] = new_tile
                new_pos = check_tile(new_tile)
                if (new_pos != -1):
                    return new_tile, new_pos
    return None,None

while tiles:
    for tile_id in tiles:
        tile = tiles[tile_id]
        tile_match, match_pos = check_all_variations(tile)
        if (not tile_match):
            continue

        correct_tiles[match_pos] = tile_match
        del tiles[tile_id]
        break

min_x = min([x[0] for x in correct_tiles])
min_y = min([x[1] for x in correct_tiles])
max_x = max([x[0] for x in correct_tiles])
max_y = max([x[1] for x in correct_tiles])

#print('GRID')
#for y in range(min_y, max_y+1):
#    for x in range(min_x, max_x+1):
#        if ((x,y) in correct_tiles):
#            print('#',end='')
#        else:
#            print(' ',end='')
#    print()

top_left     = int(correct_tiles[(min_x,min_y)].id)
top_right    = int(correct_tiles[(max_x,min_y)].id)
bottom_left  = int(correct_tiles[(min_x,max_y)].id)
bottom_right = int(correct_tiles[(max_x,max_y)].id)

print('Value')
print(top_left * top_right * bottom_left * bottom_right) 

