#!/usr/bin/python3
"""A base model that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
from __init__ import storage

class BaseModel:
    """this defines all common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):

        if kwargs:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            if kwargs['__class__'] in kwargs:
                del kwargs['__class__']
            if kwargs['created_at'] in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs
                        ['created_at'],format) 
            if kwargs['updated_at'] in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs
                                                ['updated_at'],format)
            for keys, value in kwargs.items():
                setattr (self, key , value)
        else:
            id = str(uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()

    def __str__(self):
        """prints human readable description"""

        return f"({[self.__class__.__name__]} {(self.id)} {self.__dict__})"

        
    def __init__ save(self):
        """updates the last modified time of the attribute"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """converts the object to a dictionary"""

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.created_at.isoformat()
        return obj_dict

