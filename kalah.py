import string


class Kalah(object):

    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        letters_lowercase = string.ascii_lowercase
        letters_uppercase = string.ascii_uppercase
        dict_lowercase = dict(list(zip(letters_lowercase, [self.seeds] * holes))[::-1])
        dict_uppercase = dict(list(zip(letters_uppercase, [self.seeds] * holes))[::-1])

        self.board = {**dict_lowercase, 'bank_player_one': 0, **dict_uppercase, 'bank_player_tow': 0}
        self.turn = [1, 0]

    def play(self, hole):

        if self.turn[0] == 1 and hole.isupper() or self.turn[1] == 1 and hole.islower():
            raise IndexError

        if self.board[hole] == 0:
            raise ValueError

        current = hole
        i = 0
        flag = 0
        sum_of_seeds = self.board[hole]
        self.board[hole] = 0

        while i < sum_of_seeds:
            if current == 'a':
                if self.turn[0] == 1:
                    self.board['bank_player_one'] += 1
                    if sum_of_seeds - i - 1 == 0:
                        flag = 1

                else:
                    i -= 1
                current = 'G'

            elif current == 'A':

                if self.turn[1] == 1:
                    self.board['bank_player_tow'] += 1

                    if sum_of_seeds - i - 1 == 0:
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

                # if the seeds were finished when he reached an empty hole that belonged to him
                if current.isupper() and self.turn[1]:
                    temp = self.holes - (
                            ord(current) - ord('A') + 1)  # Calculates the number of holes up to the current one
                    parallel = chr(ord('a') + temp)  # Calculates the hole parallel to the current hole

                    if self.board[parallel] != 0:
                        self.board['bank_player_tow'] += self.board[parallel] + 1
                        self.board[parallel] = 0
                        self.board[current] = 0

                if current.islower() and self.turn[
                    0] == 1:  # if the seeds were finished when he reached an empty hole that belonged to him
                    temp = self.holes - (
                            ord(current) - ord('a') + 1)  # Calculates the number of holes up to the current one
                    parallel = chr(ord('A') + temp)  # Calculates the hole parallel to the current hole

                    if self.board[parallel] != 0:
                        self.board['bank_player_one'] += self.board[parallel] + 1
                        self.board[parallel] = 0
                        self.board[current] = 0

        if not flag:
            temp = self.turn[0]
            self.turn[0] = self.turn[1]
            self.turn[1] = temp

        if self.done() == True:
            i = 'a'

            while i in self.board:
                self.board['bank_player_one'] += self.board[i]
                self.board[i] = 0
                self.board['bank_player_tow'] += self.board[i.upper()]
                self.board[i.upper()] = 0
                i = chr(ord(i) + 1)

            if self.board['bank_player_one'] > self.board['bank_player_tow']:
                return 'Player 1 wins'

            elif self.board['bank_player_one'] < self.board['bank_player_tow']:
                return 'Player 2 wins'

            else:
                return 'tie'

        return f"Player {1 if self.turn[0] == 1 else 2} plays next"

    def status(self):
        return tuple(self.board.values())

    def set_status(self, new_status):
        self.board = new_status

    def done(self):
        flag_player_one = 0
        flag_player_tow = 0
        i = 'a'
        if self.turn[0] == 1:

            while i in self.board.keys():

                if self.board[i] != 0:
                    flag_player_one = 1
                    return False
                i = chr(ord(i) + 1)
        else:

            while i in self.board.keys():

                if self.board[i.upper()] != 0:
                    flag_player_tow = 1
                    return False
                i = chr(ord(i) + 1)

        return True

    def score(self):
        return (self.board['bank_player_one'], self.board['bank_player_tow'])

    def my_render(self):
        a = ' **** '
        b = '*    *'
        c = '=' * 7
        w1 = a + '  ' + c * self.holes + '   ' + a + '\n'
        w2 = '*    *' + '  ' + '|      ' * self.holes + '|' + '  ' + '*    *\n'
        w3 = b + '  '
        for k, v in self.board.items():
            if k == 'bank_player_one':
                break
            else:
                w3 += f"|  {v}{' ' if v<10 else ''}  "
        w3 += '|  ' + b + '\n'
        w = f"* {self.board['bank_player_tow']}{' ' if self.board['bank_player_tow'] < 10 else ''} *   {c * self.holes}  *{' ' if self.board['bank_player_one'] < 10 else ''}{self.board['bank_player_one']}  *\n"
        w5 = b + '  '
        flag = 0
        for k, v in self.board.items():
            if k == 'bank_player_one':
                flag = 1
            if flag and k != 'bank_player_tow' and k != 'bank_player_one':
                w5 += f"|  {v}{' ' if v<10 else ''}  "
        w5 += '|  ' + b + '\n'
        return w1 + w2 + w3 + w2 + w + w2 + w5 + w2 + w1

    def __str__(self):
        return self.my_render()

    def __repr__(self):
        return f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={0 if self.turn[0] == 1 else 1})"
