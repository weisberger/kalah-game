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
        self.turn = [1, 0]

    def play(self, hole):
        if self.turn[0] == 1 and hole.isupper():
            raise IndexError
        if self.board[hole] == 0:
            raise ValueError
        current = hole
        i = 0
        flag = 0
        sumOfseeds = self.board[hole]
        self.board[hole] = 0
        while i < sumOfseeds:
            if current == 'a':
                if self.turn[0] == 1:
                    self.board['bankPlayerone'] += 1
                    if sumOfseeds - i - 1 == 0:
                        flag = 1
                else:
                    i -= 1
                current = 'G'
            elif current == 'A':
                if self.turn[1] == 1:
                    self.board['bankPlayertow'] += 1
                    if sumOfseeds - i - 1 == 0:
                        flag = 1
                else:
                    i -= 1
                current = 'g'
            else:
                current = chr(ord(current) - 1)
                self.board[current] += 1
            i += 1
        if flag != 1:
            if self.board[chr(ord(current))] == 1:
                if current.isupper() and self.turn[1]:#if the seeds were finished when he reached an empty hole that belonged to him
                    temp = self.holes - (ord(current) - ord('A') + 1) #Calculates the number of holes up to the current one
                    Parallel = chr(ord('a') + temp) #Calculates the hole parallel to the current hole
                    if self.board[Parallel] != 0:
                        self.board['bankPlayertow'] += self.board[Parallel ] + 1
                        self.board[Parallel] = 0
                        self.board[current] = 0
                if current.islower() and self.turn[0] == 1:#if the seeds were finished when he reached an empty hole that belonged to him
                    temp = self.holes - (ord(current) - ord('a') + 1) #Calculates the number of holes up to the current one
                    Parallel = chr(ord('A') + temp) #Calculates the hole parallel to the current hole
                    if self.board[Parallel] != 0:
                        self.board['bankPlayerone'] += self.board[Parallel] + 1
                        self.board[Parallel] = 0
                        self.board[current] = 0
        if not flag:
            temp = self.turn[0]
            self.turn[0] = self.turn[1]
            self.turn[1] = temp
        if self.done() == True:
            i = 'a'
            while i in self.board:
                self.board['bankPlayerone'] += self.board[i]
                self.board['bankPlayertow'] += self.board[i.upper()]
                i = chr(ord(i) + 1)
            if self.board['bankPlayerone'] > self.board['bankPlayertow']:
                 return 'player 1 win'
            elif self.board['bankPlayerone'] < self.board['bankPlayertow']:
                 return 'player 2 win'
            else:
                 return 'tie'
        return f"Player {1 if self.turn[0] == 1 else 2} plays next"

        return

    def status(self):
        return tuple(self.board.values())

    def setStatus(self, newStatus):
        self.board = newStatus

    def done(self):
        flagPlayerOne = 0
        flagPlayerTow = 0
        i = 'a'
        while i in self.board.keys():
            if self.board[i] != 0:
                flagPlayerOne = 1
            if self.board[i.upper()] != 0:
                flagPlayerTow = 1
            i = chr(ord(i) + 1)
        return not (flagPlayerOne and flagPlayerTow)
        return


    def score(self):
        return(self.board['bankPlayerone'], self.board['bankPlayertow'])
