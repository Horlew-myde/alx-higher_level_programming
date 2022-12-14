#!/usr/bin/python3
"""
Defines class with no class or object attribute
"""


class LockedClass():
    """
    Prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"
    >>> a = LockedClass()
    >>> a.first_name = "Olumide"
    >>> a.first_name
    "Waython"
    >>> a.last_name = "Amune"
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
