#!/usr/bin/python3
class LockedClass:
    """Prevents user from isntatiating new locked class"""
    """For any attribute called 'first name"""
    __slots__ = ["first_name"]
