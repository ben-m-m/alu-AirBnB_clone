import json


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances."""
    def __init__(self):
        """Initializes a new instance of FileStorage."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the objects stored in __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key obj.__class__.__name__>.id"""
        key = obj.__class__.__name__
        obj_id = obj.id
        self.__objects[f'{key}.{obj_id}'] = obj

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                stored_data = json.load(f)
                for key, value in stored_data.items():
                    if value["__class__"] == "BaseModel":
                        self.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
