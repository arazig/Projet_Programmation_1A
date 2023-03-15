import sys 
sys.path.append("delivery_network")

from graph import graph_from_file, kruskal, tree_min_power, oriented_tree_construction
import unittest


class Test_s2Perso(unittest.TestCase):
    def test_network03(self):
        g = graph_from_file("input/network.03.in")  # test of the function kruskal in file network.03.in
        g_mst = kruskal(g)
        mst_expected = {1: [(2, 10, 1)],
                        2: [(3, 4, 1), (1, 10, 1)],
                        3: [(2, 4, 1), (4, 4, 1)],
                        4: [(3, 4, 1)]}
        self.assertEqual(g_mst.graph, mst_expected)

    def test_network02(self):  # test of the function kruskal in file network.02.in
        g = graph_from_file("input/network.02.in")
        g_mst = kruskal(g)
        mst_expected = {1: [(4, 4, 1)],
                        2: [(3, 4, 1)],
                        3: [(2, 4, 1), (4, 4, 1)],
                        4: [(3, 4, 1), (1, 4, 1)]}
        self.assertEqual(g_mst.graph, mst_expected)

    def test_TreeMinPower(self):  # test of the function tree_min_power
        g = graph_from_file("input/network.1.in")
        g_mst = kruskal(g)
        self.assertEqual(tree_min_power(oriented_tree_construction(g_mst), 3, 20), ([3, 2, 1, 8, 20], 13))

if __name__ == '__main__':
    unittest.main()




