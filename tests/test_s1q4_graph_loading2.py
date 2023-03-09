#a completer

import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertEqual(g.graph[1][0][2], 6)
        self.assertEqual(g.graph[3][1][2], 2)

    def test_network1(self):
        g = graph_from_file("input/network.01.in")
        self.assertEqual(g.nb_nodes, 7)
        self.assertEqual(g.nb_edges, 5)

if __name__ == '__main__':
    unittest.main()
