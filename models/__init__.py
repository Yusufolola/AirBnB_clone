#!/usr/bin/python3
"""this creates unique instance for your application"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

<<<<<<< HEAD
dict_class = {'BaseModel': BaseModel,
              'User': User,
              'Place': Place,
              'State': State,
              'City': City,
              'Amenity': Amenity,
              'Review': Review}
=======
from engine import file_storage
>>>>>>> 67846aa7c7c77f8e3ebeeaacddea78f0b72d8e5b
storage = self.FileStorage()
storage.reload()
