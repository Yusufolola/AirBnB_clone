#!/usr/bin/python3
"""class tthat serializes instances to a JSON file and bach to instance"""
import json
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import os


class FileStorage:
    """this serializes instances to a Json file and deserializes JSON file to instances"""

    __file_path = "file.json"

    __objects = {}
    classes ={"BaseModel", "User" ,"State", "City", "Amenity", "Place","Review"}

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
        for key in FileStorage.__objects.keys():
            dict_save[key]= FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_save, f)

    def reload(self):
        """
        A method deserializes the JSON file to __objects
        """
        #if os.path.isfile(FileStorage.__file_path):
        try:
            with open(self.__file_path, mode="r+", encoding="UTF-8") as myFile:
                data = json.load(myFile)
                for key, value in data.items(): 
                    class_obj = value['__class__']
                    if class_obj in self.classes:
                        my_class = eval(class_obj)
                        obj_instance = my_class(**value)
        except FileNotFoundError:
            return
