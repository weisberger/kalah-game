import string
import logging
import My_render

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
    game = Kalah(holes, seeds)
    str_render_game = ""
    print("\nStart game:\n\n")
    for s in steps:
        str_render_game += (game.__str__())
        str_render_game += (f"\n{game.play(s)}\n")
    return str_render_game


if __name__ == "__main__":

    for i in (2, 3):
        print(f"GAME #{i}")
        with open(f"data/game_{i}.txt") as f:
            lines = f.read().splitlines()
        steps = parse_game(lines, 6)
        print(render_game(6, 6, steps))
        print(("=" * 30 + "\n") * 5)
