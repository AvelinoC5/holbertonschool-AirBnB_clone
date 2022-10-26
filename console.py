#!/usr/bin/python3

"""Entry to command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Entry to command interpreter"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        return True

    def emptyline(self):
        """Empty line"""
        pass
