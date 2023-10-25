import random
from termcolor import colored

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = moves[0]
    their_move = moves[0]

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    pass


class RandomPlayer(Player):
    def learn(self, my_move, their_move):
        pass

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        play_move = None
        while play_move is None:
            temp_move = input("Rock, paper, scissors?\n").lower()
            if temp_move in ('rock', 'paper', 'scissors'):
                play_move = temp_move
                print("You played " + play_move + ".")
            else:
                print("Move unkown! Try again!\n")
        return play_move


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def results(self):
        if self.score1 > self.score2:
            print(colored("** You win! **\n", "green"))
        elif self.score1 < self.score2:
            print(colored("** You lose! **\n", "red"))
        else:
            print(colored("** It's a tie! **\n", "grey"))

    def single_play(self):
        self.single_play = 1
        print("Lets play one round!\n")

    def full_game(self):
        self.full_game = 3
        print("Lets play a full game!\n")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Opponent played {move2}.")
        if beats(move1, move2) is True:
            self.score1 += 1
        elif beats(move2, move1) is True:
            self.score2 += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: You: {self.score1}, Opponent: {self.score2}\n")

    def play_game(self):
        rounds = ""
        while rounds == "":
            temp_rounds = input("Would you like to play a [s]ingle round "
                                "or a [f]ull game?\n").lower()
            if temp_rounds == 's':
                rounds = 's'
            elif temp_rounds == 'f':
                rounds = 'f'
            else:
                print("Unknown Input.\n")
        if rounds == "s":
            self.single_play()
            self.total_rounds = self.single_play
        elif rounds == "f":
            self.full_game()
            self.total_rounds = self.full_game
        print("Game start!")
        for round in range(int(self.total_rounds)):
            print(f"Round {round}:")
            self.play_round()
        self.results()
        print(f"Game over!\
            \nFinal score: You: {self.score1}, Opponent: {self.score2}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
