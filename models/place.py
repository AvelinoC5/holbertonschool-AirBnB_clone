#!/usr/bin/python3
"""
Place Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inherits from BaseModel
 
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = []

    def __init__(self, *args, **kwargs):
        """ initializes parent class """
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
