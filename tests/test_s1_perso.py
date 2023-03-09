# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_Perso(unittest.TestCase):
   def test_network0_loading(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 9)

   def test_network0_connected_compo(self):
        g = graph_from_file("input/network.00.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})})

   def test_network0_node_reachable(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.get_path_with_power(1, 4, 11), [1, 2, 3, 4])
        self.assertEqual(g.get_path_with_power(1, 4, 10), None)

   def test_network0_minpower(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.min_power(6, 5)[1], 12)
        self.assertEqual(g.get_path_with_power(6, 5, g.min_power(6, 5)[1]-1), None) 
        #if the power of the truck is less than the minimum power, the function should return None
        self.assertEqual(g.get_path_with_power(6, 5, g.min_power(6, 5)[1]), g.min_power(6, 5)[0])

if __name__ == '__main__':
    unittest.main()