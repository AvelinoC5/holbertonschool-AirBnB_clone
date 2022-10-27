#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """ init Command Prompt """
    prompt = "(hbnb) "
    level = ["BaseModel", "City", "State",
             "User", "Place", "Review", "Amenity"]

    def do_EOF(self, args):
        """CTRl-D to exit\n"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return None
        elif (line not in self.level):
            print("** class doesn't exist **")
            return None
        else:
            my_inst = eval(line + "()")
            my_inst.save()
            print(my_inst.id)

