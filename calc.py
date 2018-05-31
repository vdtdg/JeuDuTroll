import pulp


class TableGain:

    # table [][]
    # g_opt = "n/c"
    # s_opt = "n/c"
    # x
    # y
    # t

    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

        self.table = [[TableGain(i, j, t) for i in range(0, y)] for j in range(0, x)]
        self.s_opt = "n/c"

        if t == 3:
            self.g_opt = 1
        elif t == -3:
            self.g_opt = -1

        if y <= 1 or x <= 1:
            tf = t + x - y
            if tf < 0:
                self.g_opt = -1
            elif tf == 0:
                self.g_opt = 0
            elif tf > 0:
                self.g_opt = 1
        elif y == x and t == 0:
            self.g_opt = 0
        else:
            self.g_opt = "n/c"

    def get_min_g(self):
        if self.x < 3 or self.y < 3:
            return self.g_opt
        g_min = self.table[0][0].g_opt
        for i in self.table:
            for j in i:
                g_min = min(g_min, j.g_opt)
        return g_min

    def get_max_g(self):
        if self.x < 3 or self.y < 3:
            return self.g_opt
        g_max = self.table[0][0].g_opt
        for i in self.table:
            for j in i:
                g_max = max(g_max, j.g_opt)
        return g_max

    def calc_gs_opt(self):
        if self.g_opt == "n/c" or self.s_opt == "n/c":
            for i in range(self.x):
                for j in range(self.y):
                    self.table[i][j].calc_gs_opt()
            # from here, every element in table knows its g_opt and s_opt
            # so now we're computing this one.
            # Here we create a maximisation problem
            pb = pulp.LpProblem(pulp.LpMaximize)

            # Declaring every variables (that will be probabilities for the mix-strategy)
            pb_vars = []
            for i in range(self.x):
                pb_vars.append(pulp.LpVariable("p"+str(i), 0, 1))

            g_min = self.get_min_g()
            g_max = self.get_max_g()
            g_opt = pulp.LpVariable("g_opt", g_min, g_max)
            
            # On rajoute au problème notre objectif
            pb += g_opt
            
            # Il faut maintenant ajouter toutes les contraintes
            # Rappel : Il faut plus de contraintes que de variables dans un simplex
            # cl stands for combinaison lineaire
            for i in range(self.y):
                cl = 0
                for j in range(self.x):
                    cl += pb_vars[j] * self.table[j][i].g_opt
                pb += g_opt <= cl

                # Rappel2 : la somme des proba = 1
                sum = 0
                for k in pb_vars:
                    sum += k
                pb += sum == 1

            # Definition of the problem is over, now let's solve it.
            pb.solve()

            # Finally, we store the results in the object.
            self.g_opt = pulp.value(pb.objective)
            self.s_opt = []
            for k in pb_vars:
                self.s_opt.append(k.varValue)
            print(self.__str__())
        else:
            pass

    def __str__(self):
        return "TableGain: x:{}, y:{}, t:{}, g_opt:{}, s_opt:{}".format(self.x, self.y, self.t, self.g_opt, self.s_opt)


if __name__ == "__main__":
    valer = TableGain(5, 5, 0)
    valer.calc_gs_opt()
    print("FINAL : {}".format(valer))
