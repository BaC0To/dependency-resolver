import unittest
from bfs_dfs_traverse import bfs_search, dfs_search


class TestDepenDencyResolver(unittest.TestCase):


    def test_resolve_package_a_bfs(self):
        """
        BFS test of package "A" on the given .json file
        """
        test_node = "A"
        test_packages = bfs_search(test_node)
        expected_packages = ["A", "B", "D", "E", "F", "G"]
        self.assertEqual(test_packages, expected_packages)
    
    def test_resolve_package_b_bfs(self):
        """
        BFS test of package "B" on the given .json file
        """
        test_node = "B"
        test_packages = bfs_search(test_node)
        expected_packages = ["B", "F"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_c_bfs(self):
        """
        BFS test of package "C" on the given .json file
        """
        test_node = "C"
        test_packages = bfs_search(test_node)
        expected_packages = ["C", "G", "H", "A", "B", "D", "E", "F"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_d_bfs(self):
        """
        BFS test of package "D" on the given .json file
        """
        test_node = "D"
        test_packages = bfs_search(test_node)
        expected_packages = ["D", "G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_e_bfs(self):
        """
        BFS test of package "E" on the given .json file
        """
        test_node = "E"
        test_packages = bfs_search(test_node)
        expected_packages = ["E"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_f_bfs(self):
        """
        BFS test of package "F" on the given .json file
        """
        test_node = "F"
        test_packages = bfs_search(test_node)
        expected_packages = ["F"]
        self.assertEqual(test_packages, expected_packages)
    
    def test_resolve_package_g_bfs(self):
        """
        BFS test of package "G" on the given .json file
        """
        test_node = "G"
        test_packages = bfs_search(test_node)
        expected_packages = ["G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_h_bfs(self):
        """
        BFS test of package "H" on the given .json file
        """
        test_node = "H"
        test_packages = bfs_search(test_node)
        expected_packages = ["H", "A", "B", "D", "E", "F", "G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_a_dfs(self):
        """
        DFS test of package "A" on the given .json file
        """
        visited = []
        test_node = "A"
        test_packages = dfs_search(visited, test_node)
        expected_packages = ['A', 'B', 'F', 'D', 'G', 'E']
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_b_dfs(self):
        """
        DFS test of package "B" on the given .json file
        """
        visited = []
        test_node = "B"
        test_packages = dfs_search(visited, test_node)
        expected_packages = ['B', 'F']
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_c_dfs(self):
        """
        DFS test of package "C" on the given .json file
        """
        visited = []
        test_node = "C"
        test_packages = dfs_search(visited, test_node)
        expected_packages = ['B', 'F', 'C', 'G', 'H', 'A', 'D', 'E']
        self.assertEqual(test_packages, expected_packages)




if __name__ == "__main__":
    unittest.main()