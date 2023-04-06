# This will work if ran from the root folder.
# various test of our function min_dist_dijkstra
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network1(self):
        g = graph_from_file("input/network.1.in")
        self.assertEqual(g.min_dist_dijkstra(19, 4, 40000), [19, 11, 2, 4])
        self.assertEqual(g.min_dist_dijkstra(19, 4, 15), [19, 5, 1, 8, 4])
        self.assertEqual(g.min_dist_dijkstra(19, 4, 10), [19])

    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.min_dist_dijkstra(1, 3, 200), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
