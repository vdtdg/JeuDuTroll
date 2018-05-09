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
