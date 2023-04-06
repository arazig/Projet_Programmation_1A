import sys 
sys.path.append("delivery_network")

from Optimal_profit import opti
import unittest


class test_optimal(unittest.TestCase):
    def test1_route1(self):
        Trucks = opti(1, 0, Budget = 200)  # test of the opti function with file routes.1.in and trucks.0.in        
        # we also note here that for a budget as low as 200 no selection is made
        self.assertEqual(Trucks, ([], 0))


if __name__ == '__main__':
    unittest.main()