#!/usr/bin/python3
"""
A custom module City that inherits from the parent BaseModel
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class City that inherits from BaseModel
    """
    state_id = "" 
    name = ""
