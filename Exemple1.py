# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:27:28 2021

@author: Emilie
"""

from constraint import *

# Dimension du problème
n = 8

# Création du problème
pb = Problem()

# Création d’une liste python cols de dimension n (numéro de colonnes associé aux tours (une tour par ligne))
cols = range(n)

# Ajout de cols dans le problème. Chaque élément de cols a pour domaine {1, ..., n}
pb.addVariables(cols, range(n))

# Ajout de la contrainte AllDiff
pb.addConstraint(AllDifferentConstraint())

# Récupération d’une solution
s = pb.getSolution()

# Récupération de l’ensemble des solutions possibles
s = pb.getSolutions()

# Affichage
print("Nombre de solutions = ", len(s))
print(s)
