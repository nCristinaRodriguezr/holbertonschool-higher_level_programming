#!/usr/bin/python3
"""
A class Student that defines a student by
"""


class Student:
    """
    Class that defines a student with public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes an object of class Student with given attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
