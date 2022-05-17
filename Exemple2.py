# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:29:02 2021

@author: Emilie
"""

from constraint import *

# Dimension du problème
n = 3

# Création du problème
pb = Problem()

# Création d’une liste python x représentant les valeurs possibles
x = range(1, n**2 + 1)

# Ajout de x dans le problème. Chaque élément de x a pour domaine {1, ..., n**2 + 1}
pb.addVariables(x, x)

# Ajout de la contrainte AllDiff
pb.addConstraint(AllDifferentConstraint())

# Variable contenant la somme de chaque ligne/colonne/diagonale
s = n * (n**2 + 1) / 2

# Ajout des contraintes du carré magique
for k in range(n):
    # ligne k
    pb.addConstraint(ExactSumConstraint(s), [x[k*n+i] for i in range(n)])
    # colonne k
    pb.addConstraint(ExactSumConstraint(s), [x[k+n*i] for i in range(n)])
    # premi`ere diagonale
    pb.addConstraint(ExactSumConstraint(s), [x[n*i+i] for i in range(n)])
    # deuxi`eme diagonale
    pb.addConstraint(ExactSumConstraint(s), [x[(n-1)*i] for i in range(1, n+1)])

solutions = pb.getSolutions()
print("Nombre de solutions = ", len(solutions))
print (solutions[0])