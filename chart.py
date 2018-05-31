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

    plt.subplot(2, 1, 1)
    # Calcule la moyenne joueur 1 sur N parties
    y1_mean = [np.mean(y1)] * len(x)
    fig, ax = plt.subplots()
    # Plot J1
    ligne_J1 = ax.plot(x, y1, label='Joueur 1', marker='o')
    # Plot J2
    ligne_J2 = ax.plot(x, y2, label='Joueur 2', marker='o')
    # Plot la moyenne de la strategie
    mean_line = ax.plot(x, y1_mean, label='Moy strat', linestyle='--')
    # Legende
    legend = ax.legend(loc='upper right')
    plt.xlabel('Nombre de parties jouées')
    plt.ylabel('Gain')
    plt.title('Evolution de la stratégie 1 pour N parties')
    plt.grid(True)


    plt.show()

    # t1 = np.arange(0.0,nb_parties, 0.1)
    # t2 = np.arange(0.0,nb_parties, 0.02)
    #
    # plt.figure(1)
    # # premiere strategie
    # plt.subplot(211)
    # plt.plot(t1, f(t1,nb_parties), 'bo', t2, f(t2,nb_parties), 'k')
    #
    # #deuxieme strategie
    # plt.subplot(212)
    # plt.plot(t2, np.cos(2 * np.pi * t2), '-ok')
    # plt.show()

if __name__ == '__main__':
    # main()
     affiche_graphe(strategieValerianGauche, strategieValerianDroit, 10)