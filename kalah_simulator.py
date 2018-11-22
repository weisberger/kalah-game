import string
import logging

from kalah import Kalah


def parse_game(lines, holes):
    cu = ord('A') + holes - 1
    cl = ord('a') + holes - 1

    list_moves = []
    for line in lines:

        for letter in line:

            if letter.isalpha():

                if letter.isupper():
                    list_moves.append(chr(ord('A') + (cu - ord(letter))))

                else:
                    list_moves.append(chr(ord('a') + (cl - ord(letter))))

    print(list_moves)
    return list_moves


def simulate_game(holes, seeds, steps):

    game = Kalah(holes, seeds)
    list_simulate_game = []

    for s in steps:
        list_simulate_game.append((game.play(s), game.status()))

    return list_simulate_game


def render_game(holes, seeds, steps):
    pass


if __name__ == "__main__":
    pass

