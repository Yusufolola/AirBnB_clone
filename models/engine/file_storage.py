#!/usr/bin/python3
"""class tthat serializes instances to a JSON file and bach to instance"""
import JSON
import models
from models.base_model import BaseModel
from models.user import User
import os


class FileStorage:
    """this serializes instances to a Json file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method that returns the dictionary __object
        """
        returns (self.__objects)

    def new(self, obj):
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


