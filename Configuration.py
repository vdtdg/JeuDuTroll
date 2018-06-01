import pulp
import pickle


class Configuration:

    def __init__(self, x, y, t, m):
        self.x = x
        self.y = y
        self.t = t
        self.g_opt = "n/c"
        self.s_opt = "n/c"
        self.m = m
        self.mp = m // 2

        if t == self.mp:
            self.g_opt = 1
        elif t == -self.mp:
            self.g_opt = -1

        if y <= 1 or x <= 1:
            self.s_opt = [1]
            tf = t + x - y
            if tf < 0:
                self.g_opt = -1
            elif tf == 0:
                self.g_opt = 0
            elif tf > 0:
                self.g_opt = 1
        elif y == x and t == 0:
            self.g_opt = 0

    def calc_gs_opt(self, table_conf):
        # Tout d'abord, on crée notre table 'locale' de g_opt correspondant à tous les prochains coups possibles
        table_locale = dict()
        for i in range(1, self.x + 1):
            for j in range(1, self.y + 1):

                if i < j:
                    troll = self.t - 1
                    if troll < -self.mp:  # Au cas où le troll va a + ou - (m' + 1)
                        troll = -self.mp
                elif i > j:
                    troll = self.t + 1
                    if troll > self.mp:
                        troll = self.mp
                else:
                    troll = self.t

                table_locale[i, j] = table_conf[self.x - i, self.y - j, troll].g_opt

        # On crée un problème linéaire de maximisation avec PuLP
        plne = pulp.LpProblem("calc", pulp.LpMaximize)

        # Déclaration de toutes les variables (qui seront nos probabilités de strategie mixte). avec 1 <= i <= self.x,
        # on a 0 <= pi <= 1
        plne_vars = dict()
        for i in range(1, self.x + 1):
            plne_vars[i] = pulp.LpVariable("p"+str(i), lowBound=0, upBound=1)

        g_opt = pulp.LpVariable("gain_opt", lowBound=-1, upBound=1)

        # On rajoute au problème notre objectif
        plne += g_opt

        # Il faut maintenant ajouter toutes les contraintes.
        # cl pour combinaison lineaire
        for j in range(1, self.y + 1):
            cl = 0
            for i in range(1, self.x + 1):
                cl += table_locale[i, j] * plne_vars[i]  # A RE RE RE VERIFIER
            plne += cl >= g_opt

        # Rappel2 : la somme des proba = 1
        somme_proba = 0
        for k in plne_vars:
            somme_proba += plne_vars[k]
        plne += somme_proba == 1

        # Après avoir défini le problème, on le résout.
        plne.solve()

        # Finalement, on récupère les résultats
        self.g_opt = pulp.value(plne.objective)
        self.s_opt = dict()
        for k in plne_vars:
            self.s_opt[k] = plne_vars[k].varValue
        # print(self.__str__())

    def __str__(self):
        return "Configuration: x:{}, y:{}, t:{}, g_opt:{}, s_opt:{}".format(self.x, self.y, self.t, self.g_opt, self.s_opt)


def export_fichier(n, m, dict_a_sauv):
    # On transforme le dict de configuration en un dict simple de s_opt.
    dict_s_opt = dict()
    for key in dict_a_sauv:
        dict_s_opt[key] = dict_a_sauv[key].s_opt

    with open('data/{}-{}-{}.json'.format(n, n, m), 'wb') as conf_file:
        pickle.dump(dict_s_opt, conf_file)


def main():
    N = 50
    m = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for M in m:
        # M = 7
        Mp = M // 2
        table = dict()
        # Les cas triviaux sont initialisés lors de la creation de chaque configuration
        for i in range(N + 1):
            for j in range(N + 1):
                for k in range(-Mp, Mp + 1):
                    table[i, j, k] = Configuration(i, j, k, M)

        # Puis on calcule le g_opt et s_opt de toutes les configurations en allant des plus petites aux plus grandes.
        for y in range(2, N + 1):
            for x in range(2, N + 1):
                for t in range(-Mp + 1, Mp):
                    table[x, y, t].calc_gs_opt(table)

        print(table[N, N, 0].__str__())
        export_fichier(N, M, table)


if __name__ == "__main__":
    main()
