import unittest

from read_from_json import read_json_file
from list_of_dicts_to_single_dict import package_to_dict
from depth_first_search_travers import depth_first_search


class TestDepenDencyResolver(unittest.TestCase):


    def test_resolve_package_a(self):
        """
        DFS test of package "A" on the given .json file
        """
        test_node = "A"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["A", "B", "F", "D", "G", "E"]
        self.assertEqual(test_packages, expected_packages)
    
    def test_resolve_package_b(self):
        """
        DFS test of package "B" on the given .json file
        """
        test_node = "B"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["B", "F"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_c(self):
        """
        DFS test of package "C" on the given .json file
        """
        test_node = "C"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["C", "G", "H", "A", "B", "F", "D", "E"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_d(self):
        """
        DFS test of package "D" on the given .json file
        """
        test_node = "D"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["D", "G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_e(self):
        """
        DFS test of package "E" on the given .json file
        """
        test_node = "E"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["E"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_f(self):
        """
        DFS test of package "F" on the given .json file
        """
        test_node = "F"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["F"]
        self.assertEqual(test_packages, expected_packages)
    
    def test_resolve_package_g(self):
        """
        DFS test of package "G" on the given .json file
        """
        test_node = "G"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_h(self):
        """
        DFS test of package "H" on the given .json file
        """
        test_node = "H"
        test_packages = depth_first_search([], package_to_dict(read_json_file()), test_node)
        expected_packages = ["H", "A", "B", "F", "D", "G", "E"]
        self.assertEqual(test_packages, expected_packages)

        
if __name__ == "__main__":
    unittest.main()