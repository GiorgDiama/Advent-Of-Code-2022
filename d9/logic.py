import math
import sys

def visualize(head, tail):
    if '-v' in sys.argv:
        try:
            idx = sys.argv.index('-v') + 1
            grid_boarder = int(sys.argv[idx])
        except IndexError as e:
            grid_boarder = 15

        grid =  [['.' for _ in range(-grid_boarder, grid_boarder)] for _ in range(-grid_boarder, grid_boarder)]

        if isinstance(tail, list):
            for indx, knot in enumerate(reversed(tail)):
                x = int(knot[0]) + grid_boarder
                y = int(knot[1]) + grid_boarder
                grid[-y][x] = len(tail) - indx

            grid[-head[1]+grid_boarder][head[0]+grid_boarder] = "H"
        else:
            grid[tail[0]+grid_boarder][tail[1]+grid_boarder] = "T"
            grid[head[0]+grid_boarder][head[1]+grid_boarder] = "H" if grid[head[0]+grid_boarder][head[1]+grid_boarder] == '.' else "O" 

        for row in grid:
            print(*row)

        input("next?")

# tuple operations
add = lambda x, y: (x[0] + y[0], x[1] + y[1])
ecl_distance = lambda x, y : math.sqrt(math.pow(x[0]-y[0],2) + math.pow(x[1]-y[1], 2))

def first():
    data = [x[:-1] for x in open('input.txt')]

    '''
        Logic:
            Visisted: set of unique positions that the tail has visited
            head: position of head
            tail: position of tail

            - Simulate each head move
            - if distance between head and tail >= 2
                - move tail to heads old position
            - If tail moves to a spot for the first time (i.e that spot is not in Visited)
            -   add that spot to Visited

            results: the length of Visited
    '''

    # map of letters to tuple
    head_moves = {"D": (0, -1), "U": (0, +1), "L": (-1,0), "R": (+1, 0)}

    visited = [] # holds points tail has visited
    head, tail = (0, 0), (0, 0) # initial positions

    # simulating rope physics
    for dir, steps in map(lambda x: x.split(' '), data[:]):
        for _ in range(int(steps)):
            # store old head pos and move head head
            old_head, head = head, add(head, head_moves[dir])
            # tail: if head stops touching tail -> move tail to old heads position
            if ecl_distance(head,tail) >= 2:
                tail = old_head
                # if tail is a new spot -> add that stop to the visited list
                if tail not in visited:
                    visited.append(tail)

            visualize(head, tail)

    print(len(visited))

def second():
    data = [x[:-1] for x in open('input.txt')]

    # map of letters to vectors
    head_moves = {"D": (0, -1), "U": (0, +1), "L": (-1,0), "R": (+1, 0)}

    visited = [] # holds points tail has visited
    rope = [(0,0) for _ in range(10)]
    
    # calculate move vectors
    move_x = lambda x, y : math.copysign(1, x[0] - y[0]) if x[0] - y[0] != 0 else 0
    move_y = lambda x, y : math.copysign(1, x[1] - y[1]) if x[1] - y[1] != 0 else 0 

    # simulating rope physics
    for dir, steps in map(lambda x: x.split(' '), data[:]):
        for _ in range(int(steps)):
            # move head
            rope[0] = add(rope[0], head_moves[dir])
            
            # calculate movement of the rest of the rope
            for i in range(1, len(rope)):                
                # if we need to move
                if ecl_distance(rope[i-1], rope[i]) >= 2:
                    move = (move_x(rope[i-1], rope[i]), move_y(rope[i-1], rope[i]))
                    rope[i] = add(rope[i], move)
                    
                    visualize(rope[0], rope[1:])
                    
            # check tail position
            if rope[-1] not in visited:
                visited.append(rope[-1])

    print(len(visited))

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()