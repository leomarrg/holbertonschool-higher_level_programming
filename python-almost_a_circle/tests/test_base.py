import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_instance(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_create_instance_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        json_string = Base.to_json_string([d])
        expected_json_string = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        self.assertEqual(json_string, expected_json_string)

    def test_from_json_string(self):
        json_string = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        list_dicts = Base.from_json_string(json_string)
        expected_list_dicts = [{'x': 2, 'y': 8, 'id': 1, 'width': 10, 'height': 7}]
        self.assertEqual(list_dicts, expected_list_dicts)

    def test_create_instance_from_json(self):
        json_string = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        list_dicts = Base.from_json_string(json_string)
        instances = [Base.create(**d) for d in list_dicts]
        expected_instance = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(instances[0].to_dictionary(), expected_instance.to_dictionary())

    def test_save_to_file(self):
        r = Rectangle(10, 7, 2, 8)
        r.save_to_file([r])
        filename = "Rectangle.json"
        with open(filename, 'r') as file:
            content = file.read()
        expected_content = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        self.assertEqual(content, expected_content)

    def test_load_from_file(self):
        r = Rectangle(10, 7, 2, 8)
        r.save_to_file([r])
        instances = Base.load_from_file()
        expected_instance = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(instances[0].to_dictionary(), expected_instance.to_dictionary())

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
