#!/usr/bin/python3
"""A base model that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """this defines all common attributes and methods for other classes"""

    def __init__ (self, id ,created_at, updated_at):
        """ instantiating the attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints human readable description"""

        print([self.__class__.__name__] (self.id) self.__dict__)

        
    def save(self):
        """updates the last modified time of the attribute"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """converts the object to a dictionary"""

        obj_dict = self.__dict__.copy()
        obj_dict.__class__ = self.__class__.__name__
        obj_dict.created_at = self.created_at.isoformat()
        obj_dict.updated_at = self.created_at.isoformat()
        return obj_dict

