#!/usr/bin/python3
"""
Command Line Interpreter for the AirBNB clone
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command Line Interpreter for the AirBNB clone
    """
    prompt = "(hbnb)"

    def do_help(self, arg):
        """prints helpful info on usable commands"""
        if arg == "quit":
            print("Quit command to exit the program\n")
        elif arg == "EOF":
            print("EOF: End Of File command to quit the program\n")
        elif arg == "help":
            print("Print helpful commands and their description\n")
        elif arg == "":
            print("Documented commands (type help <topic>):")
            print("=======================================")
            print("EOF help quit\n")

    def do_quit(self, arg):
        """exits the program"""
        return True

    def do_EOF(self, arg):
        """same as quit: exits the program"""
        return True

    def emptyline(self):
        """prevents the execution of the last command"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
