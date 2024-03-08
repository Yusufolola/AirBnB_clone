#!/usr/bin/python3
"""
A custom module Place that inherits from the parent BaseModel
"""
import models
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class Place that inherits from the parent BaseModel
    """
    city_id = ""  # to be used as the City.id
    user_id = ""  # to be used as the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # to be used as the list[str] of Amenity.id
