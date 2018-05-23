import random
from math import floor

def strategieValerianGauche(partie, partiesPrecedentes):
    stockActuel = partie.stockGauche
    if partie.stockDroite == partie.stockInitial / 2:
        return min(partie.stockDroite/2, stockActuel)
    else:
        return min(1, stockActuel)


def strategieValerianDroit(partie, partiesPrecedentes):
    stockActuel = partie.stockDroite
    if partie.stockGauche == partie.stockInitial / 2:
        return min(partie.stockGauche / 2, stockActuel)
    else:
        return min(2, stockActuel)


def strategiePrudente(partie, partiesPrecedentes):
    pass


def renvoieCinq(partie, partiesPrecedentes):
    return 5


def renvoieQuatre(partie, partiesPrecedentes):
    return 4


def renvoieTrois(partie, partiesPrecedentes):
    return 3


def renvoieDeux(partie, partiesPrecedentes):
    return 2


def renvoieUn(partie, partiesPrecedentes):
    return 1


def renvoieAlea(partie=None, partiesPrecedentes=None):
    return floor(random.random() * 5)
