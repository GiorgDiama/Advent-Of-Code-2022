def first():
    # create game truth tables, score and action map
    opp_choice = {'A': 1, 'B': 2, 'C':3}
    my_choice = {'X': 1, 'Y': 2, 'Z': 3}

    game_logic = [[3, 0, 6],
            [6, 3, 0],
            [0, 6, 3]]

    score = 0

     # play the game by using the look up tables
    with open('input.txt', 'r') as f:
        for line in f:
            choices = line.strip('\n').split(' ')
            me = choices[1]
            opp = choices[0]

            score += my_choice[me]
            score += game_logic[my_choice[me]-1][opp_choice[opp]-1]
        
    print(score)

def first_oneliner():
    print(sum([[[3, 0, 6], [6, 3, 0],[0, 6, 3]][j-1][i-1] + j for i,j in [[{'A': 1, 'B': 2, 'C':3}[i], {'X': 1, 'Y': 2, 'Z': 3}[j]] for i, j in [[x.strip('\n').split(' ')[0], x.strip('\n').split(' ')[1]] for x in open('input.txt', 'r')]]]))

def second():
    # create game truth tables, score and action map
    choice_score = {'A': 1, 'B': 2, 'C':3}

    w = {'A': 'B', 'B': 'C', 'C': 'A'}
    l = {'A': 'C', 'B': 'A', 'C': 'B'}
    d = {'A': 'A', 'B': 'B', 'C': 'C'}

    actions = {'X': l, 'Y': d, 'Z': w}

    game_logic = [[3, 0, 6],
                  [6, 3, 0],
                  [0, 6, 3]]

    score = 0

    # play the game by using the look up tables
    with open('input.txt', 'r') as f:
        for line in f:
            choices = line.strip('\n').split(' ')
            me = choices[1]
            opp = choices[0]

            my_action = actions[me][opp]

            score += choice_score[my_action]
            score += game_logic[choice_score[my_action]-1][choice_score[opp]-1]
        
    print(score)

print("Answer to part:1")
first()
print(f"Answer to part:2")
second()

