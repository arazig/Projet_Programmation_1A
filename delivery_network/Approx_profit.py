 
# DEFINITION ET IMPORTATIONS
"""
 L' approche théorique la plus instinctive est dans un premier temps de trier les trajets du fichiers
 route par profit décroissant. Ensuite on parcours chacuns des trajets en lui associant le camion qui coute le moins 
 chere ayant la puissnace minimale requise. On effectue cette opération jusqu'a épuisement du budget ( ie somme des couts > B)

Avantage : si le Budget est tres grand ca nous renvoie la sollution optimale puisque il nous suffit pour chaque trajet d'acheter
le camion le moins chere sans épuiser notre budget
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

def trucks_selection(x, catalogue, Budget = 25*10e9) : 
    """
    Cette fonction permet d'effecteur une selection approché de camion qui va permetre de maximiser 
    l'utilité sous contrainte de budget. On se concentre sur le réseau d'indice x. 
    args :
        x(int)        > indice du réseau
        catalogue(int > choix du catalogue de camion
        Budget(float) > budget disponible
    output :
        Selection(list)  > liste de la selection de camion proposée
    """
    # recupération des fichiers 
    route_file = 'input/routes.' + str(x) + '.in'
    powermin_file = 'input/powermin.' + str(x) + '.in'
    trucks_file = 'input/trucks.' + str(catalogue) + '.in'

    Selection = [] 
    # Ouverture des fichier et stockage des valeurs dans des listes
    Trajets = []
    with open(route_file, "r") as route, open(powermin_file, "r") as power :
            n = int(route.readline())
            for _ in range(n):

                src, dest, utility = map(float, route.readline().split())
                pwr = int(power.readline())
                Trajets.append((src, dest, utility, pwr)) 
                #  il est aussi possible de calculer directement pwr a chaque itération sans passer par lecture des fichier powermin

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

    for trajet in Trajets:
        for truck in Trucks:
            if truck[0] >= trajet[3] and Budget >= truck[1]:
                Selection.append(truck)
                Budget -= truck[1]
                break
        if Budget < truck[1]:  # Sortie de la boucle si le budget est épuisé
            break

    return Selection


# REMARQUE : Il est assez utile de créer une fonction qui calcule l'utilité obtenue a partir d'une selelction de camion 
# afin de pouvoir effectuer des comparaisons avce d'autres méthode de résolution du problème. 

def Truck_utility(x, camions):
    """
    Cette fonction nous permet d'associer a chaque camion l'utilité maximale 
    qu'il peur engendrer sur l'intégralité des trajets d'un fichier route 

    args : 
        x(int): indice du fichier routes.x.in (de 1 à 10)
        camion(list): liste des camions selectionnés
    output :
        Trucks(list) : liste de tous les camions avec l'utilité maximal que chacun engendre
    """
    # recupération des fichiers 
    route_file = 'input/routes.' + str(x) + '.in'
    powermin_file = 'input/powermin.' + str(x) + '.in'

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
                #  il est aussi possible de calculer directement pwr a chaque itération sans passer par lecture des fichier powermin

    Trucks = []      
    for c in camions :
        pow, cost = c[0],c[1]
        umax = 0
        for trj in Trajets :
            # si la puissance du c&mion est suffisante et que l'utilité est meilleure on actualise l'utilité max
            if pow >= trj[3] and umax < trj[2] : 
                umax = trj[2]
        # on associe à chaque camion l'utilité max qu'il peut rapporter         
        Trucks.append((pow, cost, umax)) 
    return sum(t[2] for t in Trucks)

#  EXEMPLE : ------------------------------------------------------------------------
# selection du fichier routes : 
#route_file = 1
# On récupère une sélection de camions
#Liste_camion = trucks_selection(route_file, 2)
#print(Liste_camion)
# On affiche l'utilité que cette selection rapporte :
#print(Truck_utility(route_file, Liste_camion))
#-------------------------------------------------------------------------------------
