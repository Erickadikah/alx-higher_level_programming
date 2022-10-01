#!/usr/bin/python3
"""defines a base class ,"""

class Base:
    """represent the base model.
    Represents the "base" for all other classes in project.

    Attibutes:
        __nb_objects (int): the number of intatieted Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initilaze a new base.

        Args:
            id (id): the identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
