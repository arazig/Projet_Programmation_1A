import sys 
sys.path.append("delivery_network")

from Optimal_profit import opti
import unittest


class test_optimal(unittest.TestCase):
    def test_route1(self):
        Trucks = opti(1, 0, Budget = 200)  # test of the opti function with file routes.1.in and trucks.0.in        
        # on note aussi ici que pour un budget aussi faible que 200 aucune sélection n'est faite
        self.assertEqual(Trucks, ([], 0))

if __name__ == '__main__':
    unittest.main()