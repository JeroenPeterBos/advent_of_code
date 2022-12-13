moves = ["Rock", "Paper", "Scissors"]

opponent_move = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

desired_result = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
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


def should_play(opponent, desired):
    opponent_idx = moves.index(opponent)

    if desired == "Lose":
        my_idx = (opponent_idx - 1) % 3
    elif desired == "Draw":
        my_idx = opponent_idx
    elif desired == "Win":
        my_idx = (opponent_idx + 1) % 3
    
    return moves[my_idx]


with open('input.txt') as f:
    lines = f.read().splitlines()

score = 0
for game in lines:
    opponent, desired = game.split(' ')
    opponent = opponent_move[opponent]
    desired = desired_result[desired]
    me = should_play(opponent, desired)

    score += move_score[me] + result_score[desired]

print(score)
