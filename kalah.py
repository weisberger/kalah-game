import string
class Kalah(object):
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        lettersLowercase = string.ascii_lowercase
        lettersUppercase = string.ascii_uppercase
        dictLowercase = dict(zip(lettersLowercase, [self.seeds]*holes))
        dictUppercase = dict(zip(lettersUppercase, [self.seeds]*holes))
        self.board = {**dictLowercase, 'bankPlayerone': 0, **dictUppercase, 'bankPlayertow': 0}
        self.turn = (1, 0)

    def play(self, hole):
        if self.turn[0] == 1 and hole.isupper():
            raise IndexError
        return

    def status(self):
        return tuple(self.board.values())


    def done(self):
        return


    def score(self):
        return
