class Monkey:
    def __init__(self, characteristics) -> None:
        self.items = []

        self.id = None
        self.update = None
        self.rule = None

        self.from_text(characteristics)

    def from_text(self, c):
        def create_update(op, val):
            operators = {"+": lambda x, y: x+y,
                         "*": lambda x, y: x*y}
            
            return lambda x: operators[op](x, val if val.isnumeric() else x)

        self.id = int(c[0].split()[-1][:-1])
        self.items = [int(x) for x in c[1].split(':')[1].split(',')]

        expr = c[2].split('=')[-1].split()
        operator = expr[-2]
        operand =  expr[-1] 
        self.update = create_update(operator, operand)
        
        div = int(c[3].split()[-1])
        if_true = int(c[4].strip('\n').split()[-1])
        if_false = int(c[5].strip('\n').split()[-1])

        self.rule = lambda x: if_true if x % div == 0 else if_false

def first():
    data = []
    
    input = ''.join(open('input.txt')).split("\n\n")
    monkies = [Monkey(x.split('\n')) for x in input]

    for m in data:
        monkies.append(Monkey(m))
        
first()