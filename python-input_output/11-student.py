#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 9-student.py)
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance.
        """
        for key, value in json_data.items():
            setattr(self, key, value)
