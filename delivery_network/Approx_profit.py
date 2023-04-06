 
# DEFINITION ET IMPORTATIONS
"""
 L' approche théorique la plus instinctive est dans un premier temps de trier les trajets du fichiers
 route par profit décroissant. Ensuite on parcours chacuns des trajets en lui associant le camion qui coute le moins 
 chere ayant la puissnace minimale requise. On effectue cette opération jusqu'a épuisement du budget ( ie somme des couts > B)

Avantage : si le Budget est tres grand ca nous renvoie la sollution optimale puisque il nous suffit pour chaque trjet d'acheter
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
#  selection du fichier routes : 
route_file = 1
#  on récupère une sélection de camions
Liste_camion = trucks_selection(route_file, 1, 25*10e9)
print(Liste_camion)
#  On affiche l'utilité que cette selection rapporte : 1399580
print(Truck_utility(route_file, Liste_camion))


# REMARQUE : Il est assez utile de créer une fonction qui calcule l'utilité obtenue a partir d'une selelction de camion 
# afin de pouvoir effectuer des comparaisons avce d'autres méthode de résolution du problème. 
"""
def max_utility(L,x):
    
    Cette fonction nous permet de connaitre l'utilité qu'engendre uen sélection de camion sur un trajet donné.
    args : 
        L (list) : c'est la liste des camions sélectionnés au préalable
        x (int) : indice du fichier route
    return :
        umax(int or float) : l'utilité généré par notre selection pour un fichier route
    

    route_file = 'input/routes.' + str(x) + '.in'
    powermin_file = 'input/powermin.' + str(x) + '.in'
    u_opt = 0
    for camion in L : 
        umax = 0
        with open(route_file, "r") as route, open(powermin_file, "r") as power: 
            n = int(route.readline())
            for _ in range(n):
                # on récupère l'utilite et la puissance minimale de chaque trajet
                src, dest, utility = map(float, route.readline().split())
                pwr = int(power.readline())
                # si la puissance du c&mion est suffisante et que l'utilité est meilleure on actualise l'utilité max
                if camion[0] >= pwr and umax < utility : 
                    umax = utility
        u_opt += umax
    return u_opt

    
print(max_utility(trucks_selection(2,2),2))
"""


#  LES TEMPS DE CALCULS de la fonction trucks_selection en fonction des différents fichier routes

""" Output :
for x in range (1,11):
    t0 = time.perf_counter()
    print(trucks_selection(x,2))
    t1 = time.perf_counter()
    t= t1 - t0
    print (str(x)+ ": " + str(t) )


1: 0.02570429899969895
2: 1.131312251000054
3: 129.39552251000168
4: 3.3461553619999904
5: 0.7697823119997338
6: 159.58119179999994
7: 152.4702746389994
8: 125.82133894599974
9: 44.99317726300069
10: 153.22190753999894

"""





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
