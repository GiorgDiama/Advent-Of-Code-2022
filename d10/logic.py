def first():
    data = [x[:-1] for x in open('input.txt')]

    cycle, V, next = 1, 1, 20

    sum_ss = 0
    for line in data:
        inst = line[:4]

        cycle += 1 

        if cycle >= next:
            sum_ss += cycle * V
            next += 40

        if inst == "addx":
            cycle += 1
            V += int(line.split()[1])

            if cycle >= next:
                sum_ss += cycle * V
                next += 40

    print(sum_ss)

def second():
    data = [x[:-1] for x in open('input.txt')]

    screen = ['.' for x in range(40*6)]
    cycle, V, next = 0, 1, 41

    def draw(screen, cycle, V):
        pixel = cycle
        sprite = (V-1, V, V+1)
        if pixel in sprite:
            screen[pixel] = "#"
        return screen

    def check_new_line(cycle, next, V):
        if cycle == next:
            V += 40
            next += 40

        return V, next

    for line in data:
        inst = line[:4]

        cycle += 1 

        V, next = check_new_line(cycle, next, V)
        screen = draw(screen, cycle, V)

        if inst == "addx":
            cycle += 1
            V += int(line.split()[1])

            V, next = check_new_line(cycle, next, V)
            screen = draw(screen, cycle, V)

    for x in range(0, 40*6, 40):
        print(*screen[x:x+39])

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()