# python implementation of the rock paper scissors game
# the player is going to be playing against the computer
# rules: rock beats scissors, scissors beats paper, paper beats rock

import random
import sys
# keeping track of game statistics
wins = 0
losses = 0
draws = 0
# player choosing their move (rock, paper or scissors)
# putting lowercase() to move
# main game loop
while True:
    print(f'Wins {wins}, Losses {losses}, Draws {draws}')
    # playing loop
    while True:
        player_move = input(
            "Choose Rock(R), Paper(P), Scissors(S), or Quit(Q) ").lower()
        if player_move == 'q':
            # Quits the game
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # this will break out of the player input loop
        else:
            print('Please enter R(Rock), P(Paper), S(Scissors) or Q to quit the game')
# computer will randomize between 1,2,3 which will be assigned to rock, paper, and scissors.

    computer_move = random.randint(1, 3)


# implementiing game logic
    if computer_move == 1 and player_move == 'r':
        print('Draw')
        draws += 1
    elif computer_move == 1 and player_move == 'p':
        print('You won! ')
        wins += 1
    elif computer_move == 1 and player_move == 's':
        print('You lost! ')
        losses += 1
    elif computer_move == 2 and player_move == 'r':
        print('You lost! ')
        losses += 1
    elif computer_move == 2 and player_move == 'p':
        print('Draw')
        draws += 1
    elif computer_move == 2 and player_move == 's':
        print('You won! ')
        wins += 1
    elif computer_move == 3 and player_move == 's':
        print('Draw')
    elif computer_move == 3 and player_move == 'p':
        print('You lost! ')
        losses += 1
    elif computer_move == 3 and player_move == 'r':
        print('You won! ')
        wins += 1
