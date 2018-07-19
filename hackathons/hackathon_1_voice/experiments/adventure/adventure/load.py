
import os
from adventure.data import parse
from adventure.game import Game
from adventure.prompt import install_words

def load_advent_dat(data):

    datapath = os.path.join(os.path.dirname(__file__), 'advent.dat')
    with open(datapath, 'r', encoding='ascii') as datafile:
        parse(data, datafile)


def resume(savefile, quiet=False):
    global _game



    _game = Game.resume(savefile)
    install_words(_game)
    if not quiet:
        print('GAME RESTORED\n')
