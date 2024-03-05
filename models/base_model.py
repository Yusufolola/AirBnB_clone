#!/usr/bin/python3
"""A base model that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """this inherits from cmd"""

    def __init__ (id ,created_at, updated_at):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.created_at = self.created_at.isoformat()
        self.updated_at = datetime.now()
        self.updated_at = self.update_at.isoformat()

    def __str__(self):
        print([] (self.id) self.__dict__)

        
    def save(self):
    def to_dict(self):

