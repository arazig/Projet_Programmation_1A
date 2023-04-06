"""
Ce fichier contient des tests relatifs à la selection de camion selon la méthode 
approhé pour resoudre le probleme d'optimisation d'utilité sous contrainte de budget
"""
import sys 
sys.path.append("delivery_network")

from Approx_profit import trucks_selection, Truck_utility
import unittest


class test_approx(unittest.TestCase):
    # l'idée est de montrer a travers ces test comment varie l'utilité en fonction de notre budget
    # test of the trucks_selection function with file routes.1.in and trucks.0.in
    def test1_route(self) :
        Trucks = trucks_selection(1, 0, Budget = 100)
        Utilite = Truck_utility(1,Trucks)
        self.assertEqual(Trucks, [])
        self.assertEqual(Utilite, 0)

    def test2_route(self) :
        Trucks = trucks_selection(1, 0, Budget = 200000)
        # selection d'un budget tout juste suffisant pour un camion
        Utilite = Truck_utility(1,Trucks)
        self.assertEqual(Trucks, [(2000000, 200000)])
        self.assertEqual(Utilite, 9997)
    
    def test3_route(self) :
        Trucks = trucks_selection(1, 0, Budget = 25*10e9)
        # selection d'un budget tout juste suffisant pour un camion
        Utilite = Truck_utility(1,Trucks)
        self.assertEqual(Trucks, [(2000000, 200000)])
        self.assertEqual(Utilite, 9997)

if __name__ == '__main__':
    unittest.main()