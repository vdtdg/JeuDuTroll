import random
from math import floor

def strategiePrudente(partie=None, partiesPrecedentes=None):
    pass


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

