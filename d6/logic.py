def first():
    data = open('input.txt').readline()
    
    for i in range(len(data)-4):
        if len(set(data[i:i+4])) == 4:
            print(i+4)
            break

def second():
    data = open('input.txt').readline()
    
    for i in range(len(data)-14):
        if len(set(data[i:i+14])) == 14:
            print(i+14)
            break
    
print("Answer to part:1")
first()
print(f"Answer to part:2")
second()