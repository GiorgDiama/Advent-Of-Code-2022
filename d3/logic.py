def first():
    scores = []
    with open('input.txt') as f:
        for line in f:
            s1 = line[:len(line)//2]
            s2 = line[len(line)//2:-1]

            # get unique items in esting in both pocktes
            matching_items = list(set([(ord(x)) for x in s1 if x in s2]))
            # calculate values using ASCI values
            matching_items = [x-38 if x < 97 else x-96 for x in matching_items]

            scores.append(sum(matching_items))

    print(sum(scores))

def first_one_liner():
    print(sum([sum(list(set([ord(x)-38 if ord(x) < 97 else ord(x)-96 for x in spl1 if x in spl2]))) for spl1, spl2 in [[x[:len(x)//2],x[len(x)//2:-1]] for x in [x for x in open('input.txt')]]]))

def second():
    data = [x.strip() for x in open('input.txt')]

    # split in groups
    cnt = 0
    groups = []
    while cnt+3 <= len(data):
        groups.append(data[cnt:cnt+3])
        cnt += 3
    # for each group find value of bagde item and add to sum
    sum = 0
    for group in groups:
        group_id = [ord(x)-38 if ord(x) < 97 else ord(x)-96 for x in group[0] if x in group[1] and x in group[2]]
        sum += group_id[0]

    print(sum)

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()