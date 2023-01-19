# python implementation of the rock paper scissors game
# the player is going to be playing against the computer
# rules: rock beats scissors, scissors beats paper, paper beats rock

import random
import sys
# player choosing their move (rock, paper or scissors)
# putting lowercase() to input
player_input = input("Choose Rock(R), Paper(P), or Scissors(S) ").lower()
# computer will randomize between 1,2,3 which will be assigned to rock, paper, and scissors.
computer_input = random.randint(1, 3)

# implementiing game logic
if computer_input == 1 and player_input == 'r':
    print('Draw')
elif computer_input == 1 and player_input == 'p':
    print('You won! ')
elif computer_input == 1 and player_input == 's':
    print('You lost! ')
elif computer_input == 2 and player_input == 'r':
    print('You lost! ')
elif computer_input == 2 and player_input == 'p':
    print('Draw')
elif computer_input == 2 and player_input == 's':
    print('You won! ')
elif computer_input == 3 and player_input == 's':
    print('Draw')
elif computer_input == 3 and player_input == 'p':
    print('You lost! ')
elif computer_input == 3 and player_input == 'r':
    print('You won! ')
