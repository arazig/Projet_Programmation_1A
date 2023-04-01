"""
Ce programme permet ce créer des fichier powermin.x.in afin de stocker la puissance minimale pour chaque trajets
des fichiers routes.x.in correspondant.
"""

# Importation :
from graph import Graph, graph_from_file, kruskal, oriented_tree_construction, tree_min_power
import time
from random import randint
import sys
sys.setrecursionlimit(5000000)


#################################################################
#######  1ere METHODE : Une sollution approchée du problème  ####
#################################################################


#  Création des fichier de puissance minimales associées a chaque trajet


def power_min_file(x):
    """
    creation a power file in the format power.x.in associated of a routes.x.in
    params :
        x (int) : index of each file
    """

    directory_path_in = "/Users/aminerazig/Desktop/ENSAE 1A/INFO/Projet_Programmation_1A/input/"
    data_path = "input/"

    g = graph_from_file(data_path + 'network.'+str(x)+'.in')
    or_tree = oriented_tree_construction(kruskal(g))

    route_file = data_path + 'routes.' + str(x) + '.in'
    powermin_file = data_path + 'powermin.' + str(x) + '.in'

    #  Ouverture du fichier 
    with open(powermin_file , "w") as out :

        with open(route_file, "r") as file :
            n = file.readline().split()
            n = int(n[0])            #  numbers of trips
            lines =file.readlines()  #  c'est une liste de lignes ["1 2 3","2 3 5"]
            out.write(str(n) + "\n") #  la première ligne du fichier se compose du nombre de trajets 
            for line in lines[0:n-1] :
                line = line.split()

                if len(line)==3 :
                    src, dest, weight = map(float,line) # Choice of parameters
                    p = tree_min_power(or_tree, src, dest)[1]
                
                else :
                        raise Exception("Incorrecte format")
                out.write(str(p) + "\n")

            # on ajoute manuellement la derniere ligne
            line = lines[n-1].split()
            if len(line)==3 :
                    src, dest, weight = map(float,line) # Choice of parameters
                    p = tree_min_power(or_tree, src, dest)[1]
                
            else :
                    raise Exception("Incorrecte format")
            out.write(str(p) )

for i in range (1,11) :
    power_min_file(i)