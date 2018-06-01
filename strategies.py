import random
import pickle
import numpy as np


def strategiePrudente(partie=None, partiesPrecedentes=None):
    n = partie.stockInitial
    m = partie.nombreCases
    with open('data/{}-{}-{}.json'.format(50, 50, m), 'rb') as conf_file:
        a = pickle.load(conf_file)
    p1 = partie.stockGauche
    p2 = partie.stockDroite
    t = partie.positionTroll
    s_opt = a[p1, p2, t]
    return np.random.choice(np.arange(1, p1, 1), p=s_opt)


def renvoieCinq(partie=None, partiesPrecedentes=None):
    return 5


def renvoieQuatre(partie=None, partiesPrecedentes=None):
    return 4


def renvoieTrois(partie=None, partiesPrecedentes=None):
    return 3


def renvoieDeux(partie=None, partiesPrecedentes=None):
    return 2


def renvoieUn(partie=None, partiesPrecedentes=None):
    return 1


def renvoieAlea(partie=None, partiesPrecedentes=None):
    return random.randint(1, partie.stockGauche)


def renvoieAleaMieux(partie=None, partiesPrecedentes=None):
    if partie.stockGauche < 5:
        return partie.stockGauche
    else:
        return random.randint(1, 5)

