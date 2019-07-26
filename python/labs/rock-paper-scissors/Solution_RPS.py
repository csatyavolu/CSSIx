#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random


def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    return raw_input("Choose your move [r|p|s]: ").lower()


def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    return "rps"[random.randint(0,2)]


def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    if player_move == comp_move:
        return "tie"
    elif (player_move == "r" and comp_move == "s") or \
         (player_move == "s" and comp_move == "p") or \
         (player_move == "p" and comp_move == "r"):
        return "player"
    else:
        return "computer"


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    print("Player Score: %s" % player_wins)
    print("Computer Score: %s" % comp_wins)
    print("Ties: %s" % ties)


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""
    if short_move == 'r':
        return "Rock"
    elif short_move == 'p':
        return "Paper"
    else:
        return "Scissors"


# Write your code below - make RPS happen using the functions above!

user_inp = int(raw_input("How many rounds do you want to play?"))
player_wins = 0
comp_wins = 0
ties = 0
for i in range(user_inp):
  print("\nGet ready to play game " + str(i+1))
  player_move = get_player_move()
  comp_move = get_computer_move()
  print("Your move was " + get_move_name(player_move))
  print("Computer's move was " + get_move_name(comp_move))
  game = determine_winner(player_move, comp_move)
  if(game == "tie"):
    ties += 1
    print("It was a tie!!")
  elif(game == "player"):
    player_wins += 1
    print("You won!!!")
  else:
    comp_wins += 1
    print("Computer won!!!")

print("\nFinal scoreboard")
print_scoreboard(player_wins, comp_wins, ties)