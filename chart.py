import troll
import strategies
import matplotlib.pyplot as plt
import numpy as np


def resultat_parties(strat1, strat2, nb_partie, nb_pierre, nb_case):
    resultats = []
    for i in range(nb_partie):
        resultats.append(troll.jouerPartie(nb_case, nb_pierre, strat1, strat2, affichageTexte=False))
    return resultats


def compte_win_j1_j2_nul(resultats):
    tab_j1 = []
    tab_j2 = []
    tab_j3 = []
    c1, c2, c3 = 0, 0, 0
    for i in range(len(resultats)):
        if resultats[i].gagnant == 1:
            c1 += 1
        elif resultats[i].gagnant == 2:
            c2 += 1
        elif resultats[i].gagnant == 3:
            c3 += 1
        tab_j1.append(c1/(i+1))
        tab_j2.append(c2/(i+1))
        tab_j3.append(c3/(i+1))

    return tab_j1, tab_j2, tab_j3


def moyenne(tableau):
    return (sum(tableau)) / len(tableau)


def affiche_graphe(strat1, strat2, nb_parties, nb_pierre, nb_case):
    # Donnees
    x = np.arange(0, nb_parties, 1)
    resultat = resultat_parties(strat1, strat2, nb_parties, nb_pierre, nb_case)
    y1, y2, y3 = compte_win_j1_j2_nul(resultat)

    # ------ Graph ------
    plt.subplot(2, 1, 1)
    # Plot J1 et J2
    plt.plot(x, y1, label='Joueur 1')
    plt.plot(x, y2, label='Joueur 2')
    plt.plot(x, y3, label='Match Nul')

    # Legende
    plt.legend(loc='best')
    # Titre
    plt.title('Evolution des résulats en fonction des stratégies des joueurs')
    plt.xlabel('Nombre de parties jouées')
    plt.ylabel('Taux de victoire')
    plt.grid(True)

    # ------ Pie Chart ------
    plt.subplot(2, 1, 2)
    labels = 'Joueur 1', 'Joueur 2', 'Match Nul'
    sizes = [y1[nb_parties-1], y2[nb_parties-1], y3[nb_parties-1]]
    plt.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%', shadow=False, startangle=270)
    plt.axis('equal')
    # Titre
    plt.title('Recapitulatif')

    # Affichage des graphiques
    # plt.show()
    plt.savefig('graph.png')


if __name__ == '__main__':
    affiche_graphe(strategies.renvoieAleaMieux, strategies.renvoieDeux, 1000, 15, 7)
