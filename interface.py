from tkinter import *
from tkinter.ttk import Combobox
import chart
import strategies


class Interface:

    def __init__(self, fenetre):

        texte_debut = Label(fenetre, text="Choisissez les paramétres, puis lancez la simulation\n")
        texte_debut.pack()

        # Images
        self.graph = PhotoImage(file="troll.png")
        self.label = Label(fenetre, image=self.graph)
        self.label.pack()

        # Cadres pour la mise en page
        cadre_simulation = Frame(fenetre)
        cadre_simulation.pack()

        cadre_parametre = Frame(cadre_simulation, width=768, height=576, borderwidth=20)
        cadre_parametre.grid(row=0, column=1)

        cadre_strategie = Frame(cadre_simulation, width=768, height=576, borderwidth=20)
        cadre_strategie.grid(row=0, column=0)

        # Imput nombre de partie
        label_nb_partie = Label(cadre_parametre, text="Nombre de partie :")
        label_nb_partie.grid(row=0, column=0)

        self.nb_partie = StringVar()
        saisie_nb_partie = Entry(cadre_parametre, textvariable=self.nb_partie, width=5)
        saisie_nb_partie.grid(row=0, column=1)

        # Imput nombre de pierre
        label_nb_pierre = Label(cadre_parametre, text="Nombre de pierre par joueur :")
        label_nb_pierre.grid(row=1, column=0)

        self.nb_pierre = StringVar()
        saisie_nb_pierre = Entry(cadre_parametre, textvariable=self.nb_pierre, width=5)
        saisie_nb_pierre.grid(row=1, column=1)

        # Imput nombre de case
        label_nb_case = Label(cadre_parametre, text="Nombre de case entre les chateaux :")
        label_nb_case.grid(row=2, column=0)

        self.nb_case = StringVar()
        saisie_nb_case = Entry(cadre_parametre, textvariable=self.nb_case, width=5)
        saisie_nb_case.grid(row=2, column=1)

        # Listes déroulantes pour les strategies des joueurs
        liste_strategie = ("Strategie prudente", "Strategie prudente Pascal", "Strategie aléatoire", "Strategie aléatoire mieux", "Renvoie 5", "Renvoie 4", "Renvoie 3", "Renvoie 2", "Renvoie 1")

        label_strategie_j1 = Label(cadre_strategie, text="Strategie joueur 1 :")
        label_strategie_j1.grid(row=0, column=0)
        self.strategie_j1 = StringVar()
        liste_strategie_j1 = Combobox(cadre_strategie, textvariable=self.strategie_j1, values=liste_strategie, state='readonly')
        liste_strategie_j1.grid(row=1, column=0)

        label_strategie_j2 = Label(cadre_strategie, text="Strategie joueur 2 :")
        label_strategie_j2.grid(row=2, column=0)
        self.strategie_j2 = StringVar()
        liste_strategie_j2 = Combobox(cadre_strategie, textvariable=self.strategie_j2, values=liste_strategie, state='readonly')
        liste_strategie_j2.grid(row=3, column=0)

        bouton_lancer = Button(cadre_simulation, text="Lancer la simulation", command=self.lancer_simulation)
        bouton_lancer.grid(row=1, column=0, columnspan=2)

    def switch_strategie(self, nomStrat):
        switcher = {
            "Strategie prudente": strategies.strategiePrudente,
            "Strategie prudente Pascal": strategies.strategiePrudentePascal,
            "Strategie aléatoire": strategies.renvoieAlea,
            "Strategie aléatoire mieux": strategies.renvoieAleaMieux,
            "Renvoie 5": strategies.renvoieCinq,
            "Renvoie 4": strategies.renvoieQuatre,
            "Renvoie 3": strategies.renvoieTrois,
            "Renvoie 2": strategies.renvoieDeux,
            "Renvoie 1": strategies.renvoieUn
        }
        return switcher.get(nomStrat, strategies.renvoieUn)

    def lancer_simulation(self):
        print("Debug : On a appuyé sur le bouton lancer")
        chart.affiche_graphe(self.switch_strategie(self.strategie_j1.get()),
                             self.switch_strategie(self.strategie_j2.get()),
                             int(self.nb_partie.get()),
                             int(self.nb_pierre.get()),
                             int(self.nb_case.get()))
        newImage = PhotoImage(file="graph.png")
        self.label.configure(image=newImage)
        self.label.image = newImage


if __name__ == '__main__':
    fenetre1 = Tk()
    interface = Interface(fenetre1)
    fenetre1.mainloop()

