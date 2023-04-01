"""
 L' approche théorique la plus instinctive est dans un premier temps de trier les trajets du fichiers
 route par profit décroissant. Ensuite on parcours chcuns des trajets en lui associant le camion qui coute le moins 
 chere ayant la puissnace minimale requise. On effectue cette opération jusqu'a épuisement du budget ( ie somme des couts > B)

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
# ( étape effectuée au préalable dans le programme powermin_file )



###### selction d'un ensemble de camion qui approche une sollution optimal du problème

def trucks_selection(x, Budget = 25*10e9) : 
    """
    Cette fonction permet d'effecteur une selection approché de camion qui va permetre de maximiser 
    l'utilité sous contrainte de budget. On se concentre sur le réseau d'indice x. 
    args :
        x(int)        > indice du réseau
        Budger(float) > budget disponible
    output :
        Selection(list)  > liste de la selection de camion proposée
    """
    # recupération des fichiers 
    route_file = 'input/routes.' + str(x) + '.in'
    powermin_file = 'input/powermin.' + str(x) + '.in'
    trucks_file = 'input/trucks.' + str(x) + '.in'

    Selection = [] 
    # Ouverture des fichier et stockage des valeurs dans des listes
    Trajets = []
    with open(route_file, "r") as route :
        with open(powermin_file, "r") as power :
            n = int(route.readline())
            for _ in range(n):

                src, dest, utility = map(int, route.readline().split())
                pwr = int(power.readline())
                Trajets.append((src, dest, utility, pwr))

    Trucks = []      
    with open(trucks_file, "r") as trucks :   
        nb_trucks = trucks.readline()
        for _ in range(int(nb_trucks)) :
            pow, cost = map(int, trucks.readline().split())
            Trucks.append((pow, cost))

    #  tri de l'ensemble de trajets par utilité decroissante           
    Trajets = sorted(Trajets, key=lambda utility:utility[2], reverse = True)

    #  tri du catalogue de camion par couts croissant  
    Trucks = sorted(Trucks, key=lambda cost:cost[1])

    for trajet in Trajets :
            for truck in Trucks :
                if truck[0] >= trajet[3] and Budget - truck[1]>= 0:
                    chx = truck
                Budget = Budget - chx[1]
                Selection.append(chx)
            print("Budget épuisé. Voici une selection d'achat de camion")
            return(Selection)
    print("Budget épuisé. Voici une selection d'achat de camion")
    return(Selection)


print(trucks_selection(1))

# REMARQUE IL EST TRES UTILE DE CREER UNE FONCTION QUI PERMET DE CALCULER L'utilité obtenue a partir d'une selelction de camion 
# ou bien de directement la calculer ne emme temps que l'on donne la selection. 



"""
pseudo-code  explication : 
on lis en simulatané les fichier route et power et on assoccie les valeusr des deux fichier dnas une liste de tuples L
on trie la liste obtenue par utilité decroissante 
on parcours les élemenst de cette liste 
on trie le fichier trucks par couts décroissant
tant que le budget est positif >0 :
    on sélectionne le camion qui coute le moins chere avec une puissance adéquate (on parcours la liste trié et on prend le 1er qui est compatible)
    condition : Truck[0] >= L[puissancemin]
        Si  Budget >= Couts :
            budget = budget - cout
            trks_selection.append(truck)
        else : 
            print("budget épuisé, voici une selction d'achat de camion : ")
            return trks_selection


"""


#################################################################
#######  2nd METHODE : Une sollution optimale du problème    ####
#################################################################