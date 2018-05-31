import troll
from strategies import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
     p = troll.Partie(7, 15)

     while p.gagnant == 0:
         g = int(input("Nombre de pierre joueur gauche : "))
         d = int(input("Nombre de pierre joueur droite : "))
         p.tourDeJeu(g, d)
         print(p)


def compte_win_j1(strat1,strat2,nb_parties):
    tab_1 = []
    for i in range(nb_parties):
        p = troll.jouerPartie(7, 15, strat1, strat2)
        if p.gagnant == 1:
            tab_1.append(1)
        else:
            tab_1.append(0)
    return tab_1

def compte_win_j2(strat1,strat2,nb_parties):
    tab_2 = []
    for i in range(nb_parties):
        p = troll.jouerPartie(7, 15,strat1, strat2)
        if p.gagnant == 2:
            tab_2.append(1)
        else:
            tab_2.append(0)
    return tab_2

def moyenne(tableau):
    return (sum(tableau))/ len(tableau)

def affiche_graphe(strat1,strat2,nb_parties):
    # Donnees
    x = np.arange(0, nb_parties, 1)
    y1 = compte_win_j1(strat1, strat2, nb_parties)
    y2 = compte_win_j2(strat1, strat2, nb_parties)
    # Calcule la moyenne joueur 1 sur N parties
    y1_mean = [np.mean(y1)] * len(x)

    # ------ Strategie 1 ------
    plt.subplot(1, 2, 1)
    # Plot J1 et J2
    plt.plot(x, y1, label='Joueur 1', marker='o')
    plt.plot(x, y2, label='Joueur 2', marker='o')

    # Plot la moyenne de la strategie
    plt.plot(x, y1_mean, label='Moy strat', linestyle='--')
    # Legende
    legend = plt.legend(loc='upper right')
    # Titre
    plt.title('Evolution de la stratégie 1 pour N parties')
    plt.xlabel('Nombre de parties jouées')
    plt.ylabel('Proba de gagner')
    plt.grid(True)

    # ------ Pie Chart ------
    plt.subplot(1, 2, 2)
    moy1 = moyenne(y1)
    moy2 = moyenne(y2)
    labels = 'Joueur 1', 'Joueur 2', 'Match Nul'
    sizes = [moy1*100, moy2*100,0]
    explode = (0, 0.1, 0) # decoupe seulement la part du joueur 2

    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')
    # Titre
    plt.title('Recapitulatif')

    # # ------ Strategie 2 ------
    # plt.subplot(2, 1, 2)
    # plt.plot(x, y1, label='Joueur 1', marker='o')
    # # Titre
    # plt.title('Evolution de la stratégie 2 pour N parties')
    # plt.xlabel('Nombre de parties jouées')
    # plt.ylabel('Proba de gagner')
    # plt.grid(True)

    # Affichage des graphiques
    plt.show()

if __name__ == '__main__':
    # main()
    # partieManuelle()
     affiche_graphe(renvoieAlea,renvoieAlea,10)