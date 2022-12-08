def first(): 
    # task: find how many trees are visible from outside the grid

    # parse data
    data = [x.strip() for x in open('input.txt')]

    # add visiblity dimension
    data = [[[int(x), 0] for x in r] for r in data]

    # for every direction for every row and colum caclulate which trees are visible      
    for row, col in zip(data, [x for x in zip(*data)]) :
        row_max_n,  row_max_r = -1, -1
        col_max_n,  col_max_r = -1, -1
        for row_n, row_r, col_n, col_r in zip(row, reversed(row),col, reversed(col)):
            if row_n[0] > row_max_n:
                row_max_n, row_n[1] = row_n[0], 1
            if row_r[0] > row_max_r:
                row_max_r, row_r[1] = row_r[0], 1
            if col_n[0] > col_max_n:
                col_max_n, col_n[1] = col_n[0], 1
            if col_r[0] > col_max_r:
                col_max_r, col_r[1] = col_r[0], 1

    # isolate visibility matrix and count visible trees
    visibility = [[x[1] for x in r] for r in data]
    print(sum([sum(x) for x in visibility]))

def second():
    def measure_view(tree_height, view):
        score = 0
        for tree in view:
            score += 1
            if tree[0] >= tree_height:
                break
        return score
    
    def calculate_scenic_score(tree, left, right, up, down):
        return measure_view(tree[0], left) * measure_view(tree[0], right) * \
            measure_view(tree[0], up) * measure_view(tree[0], down)

    data = [x.strip() for x in open('input.txt')]

    # add scenic score dimension
    data = [[[int(x), -1] for x in r] for r in data]

    # for each tree - compute the 2d views and use them to calculate scenic score 
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            row, col = data[i], [x[j] for x in data]

            left, right = reversed(row[:j]), row[j+1:]

            up, down = reversed(col[:i]), col[i+1:]
        
            tree[1] = calculate_scenic_score(tree, left, right, up, down)
    
    scenic_score = [[x[1] for x in r] for r in data]

    print(max([max(x) for x in scenic_score]))
    
print("Answer to part:1")
first()
print(f"Answer to part:2")
second()