class Tree:
    def __init__(self) -> None:
        self.root = None
        self.nodes = []

    def add_node(self, path, node):
        path = path.split('.') # get names of dirs in the path

        parent = self.root # starting on root

        parent.size += node.size # add size to every parent
        # traverse the tree to find parent
        for p in path[1:]:
            for c in parent.children:
                if c.name == p:
                    parent = c
                    break

            parent.size += node.size # add size to every parent
        # add node to tree and to a list of all dirs
        node.parent = parent
        parent.children.append(node)
        self.nodes.append(node)

    def disp_tree(self):
        self.root.disp_subtree()

class Node:
    def __init__(self, name, type, size=0) -> None:
        self.parent = None
        self.children = []
        self.name = name
        self.size = size
        self.type = type

    def __str__(self) -> str:
        return f"{self.name} | {self.size} | {self.type}"

    def __repr__(self) -> str:
        return f"{self.name} | {self.size} | {self.type}"

    def disp_subtree(self, spaces=0):
        # recursivly print a sub_tree starting on this node
        print("   "*spaces, self.__str__())
        for c in self.children:
            c.disp_subtree(spaces+1)

def build_tree(): 
    # calculate directory sizes using a tree
    data = map(lambda x:x[:-1].split(), open('input.txt'))

    t = Tree()
    # follow the commands storingthe current path and create the tree
    path = []
    for line in data:
        if line[1] == "cd":
            if line[2] == "..":
                path.pop()
            else:
                dir_name = line[2]
                if t.root is None:
                    t.root = Node(name=dir_name, type='d')
                    t.nodes.append(t.root)
                else:
                    t.add_node('.'.join(path), Node(name=dir_name, type='d'))
                    
                path.append(dir_name)
        if line[0].isnumeric():
            t.add_node('.'.join(path), Node(line[1], type='f', size=int(line[0]))) 
        
    return t

def first(): 
    # sum size of directories with size <= 100_000
    t = build_tree()
    
    sum = 0
    for n in t.nodes:
        if n.type == 'd' and n.size <= 100_000:
            sum += n.size
    
    print(sum)

def second(): 
    # if we require 30_000_00 units of free space find the size of the smallest
    # dir we can delete to get that space
    t = build_tree()

    free_space = 70_000_000 - t.nodes[0].size
    required_space = 30_000_000
    need_to_free = free_space - required_space

    candidates = []
    for d in [x for x in t.nodes if x.type == 'd' and need_to_free + x.size >= 0]:
        candidates.append([need_to_free + d.size, d])
    
    candidates = sorted(candidates, key=lambda x:x[0])
    print(candidates[0][1])

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()