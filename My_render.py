import numpy as np
import matplotlib.pylab as pl
import matplotlib as m

from kalah import Kalah


def render(nx, ny, my_data):
    a = [""]
    b = [""]

    for i in my_data.keys():

        if i.isupper():
            a.append(my_data[i])

        elif i != 'bank_player_tow' and i != 'bank_player_one':
            b.append(my_data[i])

    a.append(my_data['bank_player_tow'])
    a = a[::-1]
    b.append(my_data['bank_player_one'])
    data = [a, b]
    tb = pl.table(cellText=data, loc=(0, 0), cellLoc='center')
    tc = tb.properties()['child_artists']

    for cell in tc:
        cell.set_height(1 / ny)
        cell.set_width(1 / nx)

    ax = pl.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    pl.show()

