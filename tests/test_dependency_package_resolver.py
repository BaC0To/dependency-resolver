import unittest
from dependency_package_resolver import breadth_first_search, depth_first_search


class TestDepenDencyResolver(unittest.TestCase):


    def test_resolve_package_a(self):
        
        expected_packages = ['A', 'B', 'D', 'E', 'F', 'G']
        self.assertNotEqual(breadth_first_search(???,"A"), expected_packages)


if __name__ == '__main__':
    unittest.main()