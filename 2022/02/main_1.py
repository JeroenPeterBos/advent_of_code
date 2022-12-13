opponent_move = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

my_move = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

move_score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

result_score = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6
}

def winner(me, opponent):
    if me == opponent:
        return "Draw"
    elif me == "Rock" and opponent == "Scissors":
        return "Win"
    elif me == "Paper" and opponent == "Rock":
        return "Win"
    elif me == "Scissors" and opponent == "Paper":
        return "Win"
    else:
        return "Lose"


with open('input.txt') as f:
    lines = f.read().splitlines()

score = 0
for game in lines:
    opponent, me = game.split(' ')
    opponent = opponent_move[opponent]
    me = my_move[me]
    result = winner(me, opponent)

    score += move_score[me] + result_score[result]

print(score)
