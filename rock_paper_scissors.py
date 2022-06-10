

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class All_Rock_Player(Player):
    pass


class Reflect_Player(Player):
    """Remembers what the opponent played last round"""
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class Random_Player(Player):
    """Creates a player that chooses moves at random"""
    def move(self):
        return random.choice(moves)


class Human_Player(Player):

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        my_move = their_move

    def move(self):
        while True:
            move = input("Rock Paper Scissors > \n").lower()
            if move in moves:
                return move
            print("It's Rock Paper Scissors, chuckle-head\n")


class Cycle_Player(Player):

    def move(self):
        index = 0
        while True:
            index += 1
            if index % 2 == 0:
                return moves[index]


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = Human_Player()
        self.p2 = random.choice(players)

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}")
        print(f"Computer played: {move2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("You win the round\n")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Computer wins the round\n")
        else:
            print("It's a draw\n")

        print(f"Player 1 score: {self.p1_score}\n")
        print(f"Player 2 score: {self.p2_score}\n")

    def play_game(self):

        print("Game start!\n")
        for round in range(3):
            print(f"Round {round} --")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("~*~*~*~*~You Win!~*~*~*~*~\n")
            # print("Your score is: " + str(self.p1_score))
        elif self.p2_score > self.p1_score:
            print("~*~*~*~*~Computer Wins!~*~*~*~*~\n")
        else:
            print("It's a DRAW !\n")
        print("\nFinal Score: \n"
              "\nYou: " + str(self.p1_score) + "\n"
              "Computer: " + str(self.p2_score) + "\n")
        while True:
            play_again = input("Would you like to play "
                               "again? y/n ").lower()
            if 'y' in play_again:
                game.play_game()
            elif 'n' in play_again:
                print("Game over!\n")
                quit()


if __name__ == '__main__':
    players = [
        All_Rock_Player(),
        Random_Player(),
        Reflect_Player(),
        Cycle_Player()
        ]
    p1 = Human_Player()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
