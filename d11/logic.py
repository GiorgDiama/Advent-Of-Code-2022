import math
class Monkey:
    def __init__(self, characteristics) -> None:
        self.items = []

        self.inspect_times = 0

        self.id = None
        
        self.update = None

        self.operator = None
        self.operand = None

        self.div = None
        self.rule = None

        self.from_text(characteristics)

    def from_text(self, c):
        def create_update(op, val):
            operators = {"+": lambda x, y: x+y,
                         "*": lambda x, y: x*y}
            
            return lambda x: operators[op](x, int(val) if val.isnumeric() else x)

        self.id = int(c[0].split()[-1][:-1])
        self.items = [int(x) for x in c[1].split(':')[1].split(',')]

        expr = c[2].split('=')[-1].split()
        self.operator = expr[-2]
        self.operand =  int(expr[-1]) if expr[-1].isnumeric() else None
        self.update = create_update(expr[-2], expr[-1])
        
        self.div = int(c[3].split()[-1])
        if_true = int(c[4].strip('\n').split()[-1])
        if_false = int(c[5].strip('\n').split()[-1])

        self.rule = lambda x: if_true if x % self.div == 0 else if_false
    
def first():
    input = ''.join(open('input.txt')).split("\n\n")
    monkies = [Monkey(x.split('\n')) for x in input]

    rounds = 20
    for _ in range(rounds):
        for m in monkies:
            while m.items:
                item = m.items.pop(0)
                item = m.update(item//100)
                m.inspect_times += 1
                throw_to = m.rule(item)
                monkies[throw_to].items.append(item)
    
    top_monkies = sorted([x.inspect_times for x in monkies])[-2:]
    print(math.prod(top_monkies))

def second(): 
    input = ''.join(open('input.txt')).split("\n\n")
    monkies = [Monkey(x.split('\n')) for x in input]

    f = math.prod([x.div for x in monkies])

    rounds = 10_000

    for _ in range(rounds):
        for m in monkies:
            while m.items:
                item = m.items.pop(0)
                item = m.update(item) % f

                m.inspect_times += 1

                throw_to = m.rule(item)
                monkies[throw_to].items.append(item)

    top_monkies = sorted([x.inspect_times for x in monkies])[-2:]
    print(math.prod(top_monkies))


print("Answer to part:1")
first()
print(f"Answer to part:2")
second()