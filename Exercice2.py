# Emilie BIEGAS
# Exercice 2

from constraint import *

# Création du problème
pb = Problem()

# Ajout de variables dans le problème

# Les variables à determiner

interv = [i for i in range(10)]
pb.addVariable("A", interv)
pb.addVariable("B", interv)
pb.addVariable("C", interv)
pb.addVariable("D", interv)
pb.addVariable("E", interv)

# Les deux valeurs manquantes à droite de l'égalité
pb.addVariable("a", interv)
pb.addVariable("b", interv)

"""# Ajout de variable représentant les multiplications intermédiaires
pb.addVariable("m", intervR)
pb.addVariable("n", intervR)
pb.addVariable("o", intervR)"""

# Ajout des contraintes 173 * ABCDE = 2020a2b

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