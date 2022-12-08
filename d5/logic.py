def load_crane():
    # parse crane
    data = [x.strip('\n') for x in open('input.txt')]

    ship = data[:9]
    
    ship_dict = dict.fromkeys(ship[-1].split()) # represent stacks in a dict
    
    data = [[x for x in l] for l in ship[:-1]] # make 2d array
    data = [x for x in zip(*data)] # transpose
    
    cnt = 1 # keep track of current stack
    for line in data:
        line = [x for x in reversed(line)] # reverse to make stack (LiFo)
        if 64 < ord(line[0]) < 91: # if not a blank space add to dictionary
           ship_dict[str(cnt)] = [x for x in line if x != ' ']
           cnt += 1 
    
    return ship_dict

def first():
    # load crane and follow orders
    data = [x.strip('\n') for x in open('input.txt')]

    moves = data[10:]
    
    ship_dict = load_crane()

    for num, _from, _to in [x.split()[1::2] for x in moves]:
        # remove and append (reversing order)
        for _ in range(int(num)):
            el = ship_dict[_from].pop()
            ship_dict[_to].append(el)

    answer = ''
    for key in ship_dict:
        answer += ship_dict[key][-1]
    print(answer)

def second():
    # load crane and follow orders (this time the crane can move boxes while maintiing order)
    data = [x.strip('\n') for x in open('input.txt')]

    moves = data[10:]
    
    ship_dict = load_crane()
        
    for num, _from, _to in [x.split()[1::2] for x in moves]:
        move = ship_dict[_from][-int(num):] # get elements mainiting order
        for el in move:
            ship_dict[_from].pop() # pop el
            ship_dict[_to].append(el) # append in order
    
    answer = ''
    for key in ship_dict:
        answer += ship_dict[key][-1]
    print(answer)

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()