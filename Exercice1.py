# Emilie BIEGAS
# Exercice 1

from constraint import *

# Création du problème
pb = Problem()

# Ajout de variables dans le problème

interv = [i for i in range(10)]
pb.addVariable("O", interv)
pb.addVariable("I", interv)
pb.addVariable("U", interv)
pb.addVariable("S", interv)

# M,T,L,E et N ne prennent pas la valeur 0
intervN0 = [i for i in range(1, 10)]
pb.addVariable("M", intervN0)
pb.addVariable("T", intervN0)
pb.addVariable("L", intervN0)
pb.addVariable("E", intervN0)
pb.addVariable("N", intervN0)

# Ajout de variable représentant les retenues
intervR = [0, 1, 2, 3]
pb.addVariable("a", intervR)
pb.addVariable("b", intervR)
pb.addVariable("c", intervR)

# Ajout de la contrainte AllDiff
pb.addConstraint(AllDifferentConstraint(), "OIUSMTLEN")

# Ajout des contraintes MOI + TOI + LUI + ELLE = NOUS

pb.addConstraint(lambda i, e, s, r1: 3*i + e - 10*r1 == s, ("I", "E", "S", "a"))
pb.addConstraint(lambda o, u, l, r1, r2: 2*o + u + l + r1 - 10*r2 == u, ("O", "U", "L", "a", "b"))
pb.addConstraint(lambda m, t, l, o, r2, r3: m + t + 2*l + r2 - 10*r3 == o, ("M", "T", "L", "O", "b", "c"))
pb.addConstraint(lambda e, n, r3: e + r3 == n, ("E", "N", "c"))


solutions = pb.getSolutions()
print("Nombre de solutions = ", len(solutions))

if len(solutions) != 0:
    # Recherche de la solution avec le meilleur NOUS
    ibest = 0
    best = solutions[0]['N'] * 1000 + solutions[0]['O'] * 100 + solutions[0]['U'] * 10 + solutions[0]['S'] 
    
    for i in range(1, len(solutions)):
        if best < solutions[i]['N'] * 1000 + solutions[i]['O'] * 100 + solutions[i]['U'] * 10 + solutions[i]['S'] :
            best = solutions[i]['N'] * 1000 + solutions[i]['O'] * 100 + solutions[i]['U'] * 10 + solutions[i]['S']
            ibest = i
        
    print("La meilleure solution est : ", solutions[i], " avec un NOUS de valeur ", best)