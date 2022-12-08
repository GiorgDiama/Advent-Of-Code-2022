def first(): # find complete overlap
    with open('input.txt') as f:
        data = [[x for x in line[:-1].split(',')] for line in f]

    print(len(data))
    cnt_overlap = 0

    for d in data:
        p1 = d[0].split('-')
        p2 = d[1].split('-')
        p1_low, p1_high = int(p1[0]), int(p1[1])
        p2_low, p2_high = int(p2[0]), int(p2[1])

        dif_low = p1_low - p2_low
        dif_high = p1_high - p2_high

        '''
        case 1: perfect overlap (p1-c1 == 0 p2-c2 == 0)
            p1--------p2 
            c1--------c2

        case 2: top contained in bottom (p1 - c1 >= 0 p2-c2 <= 0) (possibility of partial point overlap to <= >=)
                p1---p2         
            c1------------c2 
        
        case 3: top contains bottom (reverse the above)
        '''
        if((dif_low == 0 and dif_high == 0) or (dif_low <= 0 and dif_high >= 0) or (dif_low >= 0 and dif_high <= 0)):
            cnt_overlap += 1

    print(cnt_overlap)

def second(): # find any overlap
        with open('input.txt') as f:
            data = [[x for x in line[:-1].split(',')] for line in f]

        print(len(data))
        cnt_overlap = 0

        for d in data:
            p1 = d[0].split('-')
            p2 = d[1].split('-')

            '''
                LOGIC: 
                    - find end point of "left area"
                    - find start point of 'right area'
                    - if they overlap -> areas overlap

                * left and right - thinking of areas as intervals on an integer axis
            '''

            areas = [[int(p1[0]), int(p1[1])], [int(p2[0]), int(p2[1])]]
            areas = sorted(areas,key=lambda x:x[0])

            if areas[0][1] >= areas[1][0]:
                cnt_overlap += 1

        print(cnt_overlap)

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()