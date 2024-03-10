#!/usr/bin/python3
"""this contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class HBNB interpreter cmd
    """
    prompt = "(hbnb)"
    classes = {"BaseModel"}

    def do_EOF(self, line):
        """input control + d to exit the program"""
        return True

    def do_exit(self, line):
        """exit the program by typing exit"""
        return True

    def postloop(self):
        """prints a new line after successful exit"""
        print ("\n")

    def do_create(self, arg):
        if len(arg) == 0:
            print(" ** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)
            new_instance = instance()
            new_instance.save()
            print("new_instance.id")









if __name__ == '__main__':
    HBNBCommand().cmdloop()
