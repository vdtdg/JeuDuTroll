import random
import pickle
import numpy as np


def strategiePrudente(partie=None, partiesPrecedentes=None):
    n = partie.stockInitial
    m = partie.nombreCases
    with open('data/{}-{}-{}.conf'.format(50, 50, m), 'rb') as conf_file:
        a = pickle.load(conf_file)
    p1 = partie.stockGauche
    p2 = partie.stockDroite
    t = partie.positionTroll
    s_opt = a[p1 + 2, p2 + 2, t - (m//2)]
    s_opt.pop()
    s_opt.pop()
    a = np.random.choice(np.arange(1, p1+1, 1), p=s_opt)
    return int(a)


def strategiePrudentePascal(partie=None, partiesPrecedentes=None):
    n = partie.stockInitial
    m = partie.nombreCases
    with open('data/{}-{}-{}.pascal'.format(50, 50, m), 'rb') as conf_file:
        a = pickle.load(conf_file)
    p1 = partie.stockGauche
    p2 = partie.stockDroite
    t = partie.positionTroll
    s_opt = a[p1, p2, t - (m//2)]
    a = np.random.choice(np.arange(1, p1+1, 1), p=s_opt)
    return int(a)


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

