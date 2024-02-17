import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_create_instance(self):
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 1)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        self.assertEqual(r.display(), expected_output)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        expected_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected_str)

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 5})

if __name__ == '__main__':
    unittest.main()
