import unittest
from name_function2 import format_name

class NamesTestCase(unittest.TestCase):
    """Testa name_function så att den gör det den ska"""

    def test_first_last_name(self):
        """accepteras ett vanligt för och efter namn som Lars Olsson"""
        full_name = format_name('lars', 'olof', 'olsson')
        self.assertEqual(full_name, 'Lars Olof Olsson')

if __name__ == '__main__':
    unittest.main()