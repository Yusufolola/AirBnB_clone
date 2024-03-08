#!/usr/bin/python3
"""class tthat serializes instances to a JSON file and bach to instance"""
import JSON

class FileStorage:
    """this serializes and deserializes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        returns (self.__objects)

    def new(self, obj):
        for key, value in obj:
            setattr(self ,key ,value)

    def save(self):
        with open(__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        if __file_path:
            with open(__file_path, 'r') as f:
                return json.load(f)
        else:
            pass


