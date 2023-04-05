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

def trucks_selection(x, catalogue, Budget = 2000000000000000) : 
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
    with open(route_file, "r") as route :
        with open(powermin_file, "r") as power :
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

t0 = time.perf_counter()
print(trucks_selection(10,2))
t1 = time.perf_counter()
t= t1 - t0
print (str(10)+ ": " + str(t) )

"""
for x in range (1,11):
    t0 = time.perf_counter()
    print(trucks_selection(x,2))
    t1 = time.perf_counter()
    t= t1 - t0
    print (str(x)+ ": " + str(t) )
"""
# REMARQUE IL EST TRES UTILE DE CREER UNE FONCTION QUI PERMET DE CALCULER L'utilité obtenue a partir d'une selelction de camion 
# ou bien de directement la calculer ne emme temps que l'on donne la selection. 


"""
1: 0.02570429899969895
2: 1.131312251000054
3: 129.39552251000168
4: 3.3461553619999904
5: 0.7697823119997338
6: 159.58119179999994
7: 152.4702746389994
8: 125.82133894599974
9: 44.99317726300069
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
