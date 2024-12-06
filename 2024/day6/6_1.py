import sys
import collections

UP    = 1
RIGHT = 2
DOWN  = 4
LEFT  = 8

MOVES = {
    UP    : [-1,  0], 
    RIGHT : [ 0, +1], 
    DOWN  : [+1,  0], 
    LEFT  : [ 0, -1], 
}

def get_next_coords(coords, direction):
    diff = MOVES[direction]
    return (coords[0] + diff[0], coords[1] + diff[1])

def turn_right(direction):
    return direction << 1 if direction != LEFT else UP

def get_square(matrix, coords):
    i, j = coords
    if i >=0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        return matrix[i][j]
    else:
        return ''

def walk_around(matrix, start_coords, direction):
    coords = start_coords
    visited = collections.defaultdict(int) 
    while 0 <= coords[0] < len(matrix) and 0 <= coords[1] < len(matrix[0]):
        visited[coords] = visited[coords] | direction
        next_coords = get_next_coords(coords, direction)
        next_square = get_square(matrix, next_coords)

        if next_square == '#':
            direction = turn_right(direction)
        else: 
            coords = next_coords

    return sum(1 for k in visited if visited[k])

def read_input(fname):
 
    matrix = []
    start_pos = (0, 0)
    i = 0
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            matrix.append(line)
            j = line.find('^')
            if j != -1:
                start_pos = (i, j)
            i += 1

    return matrix, start_pos

def main():
    fname = sys.argv[1]

    matrix, start_coords = read_input(fname)
    result = walk_around(matrix, start_coords, UP)
    print('result = ', result)

if __name__ == "__main__":
    main()