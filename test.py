#import pygame
import troll
import strategies

def partieManuelle():
    # Exemple de partie "manuelle"
    p = troll.Partie(7, 15)
    print(p)
    p.tourDeJeu(2, 4)
    print(p)
    p.tourDeJeu(3, 4)
    print(p)
    p.tourDeJeu(2, 1)
    print(p)
    p.tourDeJeu(4, 4)
    print(p)
    p.tourDeJeu(1, 2)
    print(p)




def main():
    p = troll.Partie(7, 15)

    while p.gagnant == 0:
        g = int(input("Nombre de pierre joueur gauche : "))
        d = int(input("Nombre de pierre joueur droite : "))
        p.tourDeJeu(g, d)
        print(p)


def partiAuto():
    troll.jouerPartie(7, 15, strategieValerianGauche, strategieValerianDroit)


if __name__ == '__main__':
    # main()
    # partieManuelle()
    partiAuto()
