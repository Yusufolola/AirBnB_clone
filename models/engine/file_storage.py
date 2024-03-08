#!/usr/bin/python3
"""class tthat serializes instances to a JSON file and bach to instance"""
import JSON
import models
from models.base_model import BaseModel
from models.user import User
import os


class FileStorage:
    """this serializes instances to a Json file and deserializes JSON file to instances"""

<<<<<<< HEAD
    __file_path = "file.json"
=======
    __file_path = 'file.json'
>>>>>>> 67846aa7c7c77f8e3ebeeaacddea78f0b72d8e5b
    __objects = {}

    def all(self):
        """
        Method that returns the dictionary __object
        """
        returns (self.__objects)

    def new(self, obj):
<<<<<<< HEAD
       # setattr
        """
        Custom method sets in __objects 
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        The  method that serializes __objects to the JSON file (path: __file_path)
        """
        dict_save = {}
        with open(self.__file_path, "w+", encoding="UTF-8") as myFile:
            for key, value in self.__objects.items():
                dict_save[key] = value.to_dict()
            json.dump(dict_save, myFile)

    def reload(self):
        """
        A method deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, mode="r+", encoding="UTF-8") as myFile:
                data = json.load(myFile)
            for key, value in data.items():  # **kwargs
                class_obj = value.get('__class__')
                if class_obj in models.dict_class:
                    self.__objects[key] = models.dict_class[class_obj](**value)
=======
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
>>>>>>> 67846aa7c7c77f8e3ebeeaacddea78f0b72d8e5b


