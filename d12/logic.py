class Pos:
    def __init__(self, x, y, letter) -> None:
        self.x, self.y = x, y
        self.letter = letter
        self.visited = False
        self.moves = []

    def __str__(self) -> str:
        return f"{self.pos}"

    def __repr__(self) -> str:
        return f"{self.pos}"

    @property
    def pos(self):
        return (self.x, self.y)

    def can_move(self, letter):
        return ord(self.letter) >= ord(letter) - 1

class Node:
    def __init__(self, pos) -> None:
        self.parent = None
        self.children = []
        self.pos = pos
        self.steps = 0
        self.letter = pos.letter

    def __str__(self) -> str:
        return f"{self.pos} | {self.steps} | {self.letter}"

    def __repr__(self) -> str:
        return f"{self.pos} | {self.steps} | {self.letter}"

    def disp_subtree(self, spaces=0):
        # recursivly print a sub_tree starting on this node
        print("   "*spaces, self.__str__())
        for c in self.children:
            c.disp_subtree(spaces+1)
        
    def add_child(self, node):
        node.parent = self
        node.steps = self.steps + 1
        self.children.append(node)
    
    def expand(self, positions):
        possible_moves = positions[self.pos.pos].moves

        for move in possible_moves:
            if not move.visited:
                self.add_child(Node(move))
                move.visited = True
                
def solve_bfs(stack, positions, goal):
    while stack:
        node = stack.pop(0)
        node.expand(positions)

        for c in node.children:
            if c.pos.pos == goal:
                return c

        stack += node.children

def create_position_objects(data, start, end):
    in_bounds = lambda x, y: 0 <= x[0] < len(y) and 0 <= x[1] < len(y[0])
    tup_index = lambda y, x: y[x[0]][x[1]]

    positions = {}

    for i in range(len(data)):
        for j in range(len(data[0])):
            pos = Pos(i, j, data[i][j])

            positions[(i,j)] = pos

            if pos.pos != end:
                neighbours = ((i, j-1), (i, j+1), (i-1, j), (i+1,j))

                for n in neighbours:                    
                    if in_bounds(n, data) and pos.can_move(tup_index(data, n)):
                        pos.moves.append(Pos(n[0],n[1], tup_index(data, n)))

    return positions

def first():
    data = [[x for x in line.strip('\n')] for line in open('input.txt')]

    start_x, start_y = data.index([x for x in data if 'S' in x][0]), [x for x in data if 'S' in x][0].index('S')
    start = (start_x, start_y)
    
    end_x, end_y = data.index([x for x in data if 'E' in x][0]), [x for x in data if 'E' in x][0].index('E')
    end = (end_x, end_y)

    data[start[0]][start[1]] = 'a'
    data[end[0]][end[1]] = 'z'

    positions = create_position_objects(data, start, end)

    root = Node(positions[start])
    n = solve_bfs([root], positions, end)
    print(f"Sortest path: {n.steps}")

def second():
    data = [[x for x in line.strip('\n')] for line in open('input.txt')]

    start_x, start_y = data.index([x for x in data if 'S' in x][0]), [x for x in data if 'S' in x][0].index('S')
    start = (start_x, start_y)
    
    end_x, end_y = data.index([x for x in data if 'E' in x][0]), [x for x in data if 'E' in x][0].index('E')
    end = (end_x, end_y)

    positions = create_position_objects(data, start, end)
    
    starting_positions = [x for x in positions if positions[x].letter == 'a']

    results = []
    for pos in starting_positions:
        print(f"Evaluating starting position {pos} with altitude {positions[pos].letter} ...", end='\r')
        root = Node(positions[pos])
        n = solve_bfs([root], positions, end)

        #reset positions
        positions = create_position_objects(data, start, end)
        if n is not None:
            results.append(n.steps)
        
    print(f"Exploration finished sortest path from lowest elevation: {sorted(results)[0]} steps", end='\n')

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()