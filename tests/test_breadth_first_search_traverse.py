import unittest
from breadth_first_search_traverse import breadth_first_search


class TestDepenDencyResolver(unittest.TestCase):


    def test_resolve_package_a(self):
        """
        BFS test of package "A" on the given .json file""""
        test_node = "A"
        test_packages = breadth_first_search(package_to_dict(read_json_file("package.JSON")), test_node)
        expected_packages = ['A', 'B', 'D', 'E', 'F', 'G']
        self.assertEqual(test_packages, expected_packages)

if __name__ == '__main__':
    unittest.main()