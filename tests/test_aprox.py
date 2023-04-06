"""
Ce fichier contient des tests relatifs à la selection de camion selon la méthode 
approhé pour resoudre le probleme d'optimisation d'utilité sous contrainte de budget
"""
import sys 
sys.path.append("delivery_network")

from Approx_profit import trucks_selection, Truck_utility
import unittest


class test_approx(unittest.TestCase):
    # l'idée est de montrer à travers ces tests comment varie l'utilité en fonction de notre budget
    # test de la fonction trucks_selection avec les fichiers routes.1.in et trucks.0.in
    def test1_route(self) :
        Trucks = trucks_selection(1, 0, Budget = 100)
        Utilite = Truck_utility(1,Trucks)
        self.assertEqual(Trucks, [])  # aucun camion selectionné
        self.assertEqual(Utilite, 0)

    def test2_route(self) :
        Trucks = trucks_selection(1, 0, Budget = 200000)
        # selection d'un budget tout juste suffisant pour un camion
        Utilite = Truck_utility(1,Trucks)
        self.assertEqual(Trucks, [(2000000, 200000)])
        self.assertEqual(Utilite, 9997)
    
    def test3_route(self) :
        Trucks = trucks_selection(1, 0, Budget = 25*10e9)
        Utilite = Truck_utility(1,Trucks)
        self.assertEqual(len(Trucks), 140) # une selection égale au nombre de trajets (ie tous les trajets sont couverts)
        self.assertEqual(Utilite, 1399580)
    
    def test_route1(self):
        Trucks = trucks_selection(1, 0, Budget = 2000000)  # test de la fonction trucks_selection avec les fichiers routes.1.in et trucks.0.in        
        self.assertIn(Trucks, [[(2000000, 200000), (2000000, 200000), (2000000, 200000), (2000000, 200000), 
                               (2000000, 200000), (2000000, 200000), (2000000, 200000), (2000000, 200000), 
                               (2000000, 200000), (2000000, 200000)], [(2000000, 200000), (2000000, 500000)]])
    
    def test_route3(self):
        Trucks = trucks_selection(3, 1, Budget = 20000000)  # test de la fonction trucks_selection avec les fichiers routes.3.in et trucks.1.in
        Trucks_expected= [(6500000, 910000), (6500000, 910000), (4000000, 560000), (6500000, 910000), (6500000, 910000), (4000000, 560000), (4000000, 560000), (5000000, 580000), 
                          (4500000, 570000), (4000000, 560000), (7000000, 980000), (7000000, 980000), (3500000, 430000), (7000000, 980000), (4000000, 560000), (6500000, 910000), 
                          (5000000, 580000), (4500000, 570000), (3000000, 360000), (5000000, 580000), (5500000, 740000), (9000000, 1450000), (3000000, 360000), (4000000, 560000), 
                          (3000000, 360000), (9500000, 1500000)]
        self.assertEqual(Trucks, Trucks_expected)

    def test_route7(self):
        Trucks = trucks_selection(7, 2, Budget = 2000000)  # test de la fonction trucks_selection avec les fichiers routes.7.in et trucks.2.in
        Trucks_expected= [(7797000, 389874), (8556000, 431175), (6650000, 335699), (7411000, 370983), (5297000, 267605)]
        self.assertEqual(Trucks, Trucks_expected)

if __name__ == '__main__':
    unittest.main()