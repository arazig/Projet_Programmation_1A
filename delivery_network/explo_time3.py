    """
Ce document nous permet de calculer le temps necessaire pour calculer une selection de camion approché pour le problème d'oprimisation
    """
#  IMPORTATIONS :
from Approx_profit import trucks_selection, Truck_utility
import sys 
sys.path.append("delivery_network")


#  LES TEMPS DE CALCULS de la fonction trucks_selection en fonction des différents fichier routes
for x in range (1,11):
    t0 = time.perf_counter()
    print(trucks_selection(x,2))
    t1 = time.perf_counter()
    t= t1 - t0
    print (str(x)+ ": " + str(t) )


""" Output : (en secondes)

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
