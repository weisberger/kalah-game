import string
class Kalah(object):
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        lettersLowercase = string.ascii_lowercase
        lettersUppercase = string.ascii_uppercase
        dictLowercase = dict(list(zip(lettersLowercase, [self.seeds]*holes))[::-1])
        dictUppercase = dict(list(zip(lettersUppercase, [self.seeds]*holes))[::-1])

        self.board = {**dictLowercase, 'bankPlayerone': 0, **dictUppercase, 'bankPlayertow': 0}
        self.turn = (1, 0)

    def play(self, hole):
        if self.turn[0] == 1 and hole.isupper():
            raise IndexError
        current = ord(hole)
        for i in range(self.board[hole]):
            self.board[chr(current - 1)] += 1
            current -= 1
        self.board[hole] = 0

        return

    def status(self):
        return tuple(self.board.values())


    def done(self):
        return


    def score(self):
        return
