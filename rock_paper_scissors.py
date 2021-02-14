

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    #def learn(self, my_move, their_move):
     #   self.my_move = my_move
      #  self.their_move = their_move

class Reflect_Player():
     """Remembers what the opponent played last round"""
     def __init__(self):
        self.p2 = Reflect_Player

     def remember(self, move2):
        play_round(move2)


class Random_Player():
    """Creates a player that chooses moves at random"""
    # def __init__(self):
    #    self.learn = learn


    def random_move(self):
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)


class Human_Player():

    def __init__(self):
        self.p1 = Human_Player

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        my_move = their_move

    def move(self, input):
        # move = input("Rock Paper Scissors > ")
        while True:
            move = input("Rock Paper Scissors > \n")
            if move in moves:
                return move
                break
            else:
                print("It's Rock Paper Scissors, chuckle-head\n")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move(input)
        move2 = self.p2.random_move()
        print(f"You played: {move1} "
              f"Computer played: {move2}")
        #self.p1.learn(move1, move2)
        #self.p2.learn(move2, move1)
        wins = beats(move1, move2)
        lose = beats(move2, move1)
        if wins:
            self.p1_score += 1
            print("You win the round\n")
            # print(f"Player 1 score: {self.p1_score}\n")
        elif lose:
            self.p2_score += 1
            print("Computer wins the round\n")
            # print(f"Player 2 score: {self.p2_score}\n")
        else:
            print("It's a draw\n")

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round} --")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("~*~*~*~*~You Win!~*~*~*~*~\n")
        elif self.p2_score > self.p1_score:
            print("~*~*~*~*~Computer Wins!~*~*~*~*~\n")
        else:
            print(" It's a DRAW !\n")
        print()
        play_again = input("Would you like to play"
                    " again? y/n ")
        if 'y' in play_again:
            game.play_game()
        if 'n' in play_again:
            quit()
        print("Game over!\n")


if __name__ == '__main__':
    game = Game(Human_Player(), Random_Player())
    game.play_game()
