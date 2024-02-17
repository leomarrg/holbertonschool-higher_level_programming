import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_create_instance(self):
        s = Square(5, 2, 8)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 1)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        self.assertEqual(s.display(), expected_output)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        expected_str = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s), expected_str)

    def test_update(self):
        s = Square(10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {'id': 89, 'size': 2, 'x': 3, 'y': 4})

if __name__ == '__main__':
    unittest.main()
