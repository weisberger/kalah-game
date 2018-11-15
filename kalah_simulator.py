def parse_game(lines):
    pass


def simulate_game(holes, seeds, steps):
    pass


def render_game(holes, seeds, steps):
    pass


if __name__ == "__main__":
    with open(f"data/game_2.txt") as f:
        lines = f.read().splitlines()
    steps = parse_game(lines)
    print(render_game(6, 6, steps))
