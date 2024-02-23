#!/usr/bin/python3
"""
a class LockedClass with no class or object
attribute, that prevents the user from dynamically creating new
instance attributes, except if the new instance
"""


class LockedClass:
    """
    not allowed to create new attributes unless first_name is called
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")
