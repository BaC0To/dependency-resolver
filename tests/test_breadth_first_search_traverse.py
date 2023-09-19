import unittest

from read_from_json import read_json_file
from list_of_dicts_to_single_dict import package_to_dict
from breadth_first_search_traverse import breadth_first_search


class TestDepenDencyResolver(unittest.TestCase):


    def test_resolve_package_a(self):
        """
        BFS test of package "A" on the given .json file
        """
        test_node = "A"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["A", "B", "D", "E", "F", "G"]
        self.assertEqual(test_packages, expected_packages)
    
    def test_resolve_package_b(self):
        """
        BFS test of package "B" on the given .json file
        """
        test_node = "B"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["B", "F"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_c(self):
        """
        BFS test of package "C" on the given .json file
        """
        test_node = "C"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["C", "G", "H", "A", "B", "D", "E", "F"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_d(self):
        """
        BFS test of package "D" on the given .json file
        """
        test_node = "D"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["D", "G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_e(self):
        """
        BFS test of package "E" on the given .json file
        """
        test_node = "E"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["E"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_f(self):
        """
        BFS test of package "F" on the given .json file
        """
        test_node = "F"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["F"]
        self.assertEqual(test_packages, expected_packages)
    
    def test_resolve_package_g(self):
        """
        BFS test of package "G" on the given .json file
        """
        test_node = "G"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["G"]
        self.assertEqual(test_packages, expected_packages)

    def test_resolve_package_h(self):
        """
        BFS test of package "H" on the given .json file
        """
        test_node = "H"
        test_packages = breadth_first_search(package_to_dict(read_json_file()), test_node)
        expected_packages = ["H", "A", "B", "D", "E", "F", "G"]
        self.assertEqual(test_packages, expected_packages)


if __name__ == "__main__":
    unittest.main()