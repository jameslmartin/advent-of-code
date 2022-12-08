from enum import Enum

class Move(Enum):
    X = 1
    Y = 2
    Z = 3
    A = 1
    B = 2
    C = 3

class Outcome(Enum):
    X = "lose"
    Y = "draw"
    Z = "win"

def get_your_move(opponent_move, outcome):
    move = opponent_move
    if outcome == Outcome.X:
        if opponent_move == Move.A:
            move = Move.Z
        if opponent_move == Move.B:
            move = Move.X
        if opponent_move == Move.C:
            move = Move.Y
    elif outcome == Outcome.Z:
        if opponent_move == Move.A:
            move = Move.Y
        if opponent_move == Move.B:
            move = Move.Z
        if opponent_move == Move.C:
            move = Move.X 
    return move

win = 6
lose = 0
draw = 3

def get_outcome_score(opponent_move, your_move):
    outcome = draw
    if (
        (your_move == Move.X and opponent_move == Move.C) or 
        (your_move == Move.Y and opponent_move == Move.A) or 
        (your_move == Move.Z and opponent_move == Move.B)
        ):
        outcome = win
    elif (
        (your_move == Move.X and opponent_move == Move.B) or
        (your_move == Move.Y and opponent_move == Move.C) or
        (your_move == Move.Z and opponent_move == Move.A)
        ):
        outcome = lose
    return outcome



"""
A = Rock
B = Paper
C = Scizzors

X = Lose
Y = Draw
Z = Win
"""


if __name__ == "__main__":
    with open("input.txt") as input:
        game_score = 0
        for line in input:
            opponent_move, outcome = line.strip("\n").split(" ")
            your_move = get_your_move(Move[opponent_move], Outcome[outcome])
            move_score = your_move.value
            outcome_score = get_outcome_score(Move[opponent_move], your_move)
            total_score = move_score + outcome_score
            print(total_score)
            game_score += total_score
        print(game_score)