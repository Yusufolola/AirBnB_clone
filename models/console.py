#!/usr/bin/python3
"""this contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class HBNB interpreter cmd
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """input control + d to exit the program"""
        return True

    def do_exit(self, line):
        """exit the program by typing exit"""
        return True

    def postloop(self):
        """prints a new line after successful exit"""
        print ("\n")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
