import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertTrue(isinstance(model.created_at, type(model.updated_at)))
        self.assertRaises(TypeError, BaseModel, id=123, created_at="2021-01-01T00:00:00", updated_at="2021-01-01T00:00:00")

    def test_str(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        str_repr = str(model)
        self.assertIn(model.id, str_repr)
        self.assertIn(model.name, str_repr)
        self.assertIn(str(model.my_number), str_repr)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        dict_repr = model.to_dict()
        self.assertEqual(dict_repr["__class__"], "BaseModel")
        self.assertEqual(dict_repr["id"], model.id)
        self.assertEqual(dict_repr["created_at"], model.created_at.isoformat())
        self.assertEqual(dict_repr["updated_at"], model.updated_at.isoformat())
