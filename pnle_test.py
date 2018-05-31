from pulp import *

prob = LpProblem("test1", LpMaximize)
# Variables
a = LpVariable("a", 0, 1)
b = LpVariable("b", 0, 1)
c = LpVariable("c", 0, 1)
t = LpVariable("t", lowBound=-1, upBound=1)  # pire et meilleur des cas

# Objective
prob += t

# Constraints
prob += 0*a + 0*b + -1*c >= t
prob += 0*a + 0*b + 0*c >= t  # 0 >= t
prob += 1*a + 0*b + 0*c >= t

prob += a + b + c == 1

# si il y a plus de variable il faut rajouter somme = 1
prob.solve()
# GLPK.solve(prob)

# Solution
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("objective=", value(prob.objective))
