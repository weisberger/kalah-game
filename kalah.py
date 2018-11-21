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

        if self.turn[0] == 1 and hole.isupper():
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
                self.board['bank_player_tow'] += self.board[i.upper()]
                i = chr(ord(i) + 1)

            if self.board['bank_player_one'] > self.board['bank_player_tow']:
                return 'player 1 win'

            elif self.board['bank_player_one'] < self.board['bank_player_tow']:
                return 'player 2 win'

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

        return f" ****   ===========================================   ****\n" \
               f"*    *  |      |      |      |      |      |      |  *    *\n" \
               f"*    *  |  {self.board['A']}{' ' if self.board['A']<10 else ''}  |  {self.board['B']}{' ' if self.board['B']<10 else ''}  |  {self.board['C']}{' ' if self.board['C']<10 else ''}  |  {self.board['D']}{' ' if self.board['D']<10 else ''}  |  {self.board['E']}{' ' if self.board['E']<10 else ''}  |  {self.board['F']}{' ' if self.board['F']<10 else ''}  |  *    *\n" \
               f"*    *  |      |      |      |      |      |      |  *    *\n" \
               f"* {self.board['bank_player_tow']}{' ' if self.board['bank_player_tow']<10 else ''} *  ===========================================  *{' ' if self.board['bank_player_one']<10 else ''}{self.board['bank_player_one']}  *\n" \
               f"*    *  |      |      |      |      |      |      |  *    *\n" \
               f"*    *  |  {self.board['a']}{' ' if self.board['a']<10 else ''}  |  {self.board['b']}{' ' if self.board['b']<10 else ''}  |  {self.board['c']}{' ' if self.board['c']<10 else ''}  |  {self.board['d']}{' ' if self.board['d']<10 else ''}  |  {self.board['e']}{' ' if self.board['e']<10 else ''}  |  {self.board['f']}{' ' if self.board['f']<10 else ''}  |  *    *\n" \
               f"*    *  |      |      |      |      |      |      |  *    *\n" \
               f" ****   ===========================================   ****\n"

    def __str__(self):
        return self.my_render()

    def __repr__(self):
        return f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={0 if self.turn[0] == 1 else 1})"
