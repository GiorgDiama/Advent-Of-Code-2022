def first():
    s = 0
    cals = []
    with open('input.txt','r') as f:
        for line in f:
            if line == '\n':
                cals.append(s)
                s = 0
            else:
                s += int(line.strip('\n'))
    
    print(max(cals))

def second():
    s = 0
    cals = []
    with open('input.txt','r') as f:
        for line in f:
            if line == '\n':
                cals.append(s)
                s = 0
            else:
                s += int(line.strip('\n'))
    
    print(sum(sorted(cals, reverse=True)[:3]))

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()