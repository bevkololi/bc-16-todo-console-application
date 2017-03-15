"""
Todo application
Todo list commands
Usage:
    my_to_do todo_create <list_name>
    my_to_do todo_open <list_param>
    my_to_do item_add <item_name>
    my_to_do list <list_name><item_name>
    my_to_do quit
    my_to_do (-i | --interactive)
    my_to_do (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import cmd
import sys
import os
import app
from docopt import docopt, DocoptExit
from termcolor import cprint, colored
from pyfiglet import figlet_format
class DocoptLanguageError(Exception):
    """Error in construction of usage-message by developer."""
def pass_opt(func):
    """
    Used to avoid repeating try and except on every docopt option.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # When a user inputs an invalid command
            # Prints the command doesn't exist
            # Also gives a proper command.
            cprint(('\nInvalid Command!'), 'magenta')
            cprint(e, 'magenta')
            print('\n')
            return
        except SystemExit:
            # automatically prints --h for help
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
class ToDoApp(cmd.Cmd):
    """The programs functionalities come here in the end"""
    intro= os.system("cls")
    cprint(figlet_format('Hello, this is your todo list!', font='slant', justify = 'centre'),
        'red', attrs=['bold', 'blink'])
    colored(__doc__)
    cprint("Type help for a list of commands. \n", 'green' )
    prompt = '<<YourTodo>>'
    file = None
    @pass_opt
    def do_todo_create(self, arg):
        """
            Command to create main todo list.
        
        Usage:
            todo_create <list_name>...
        """
        try:
            my_list = arg["<list_name>"]
            my_list_str = " ".join(my_list)           
            app.ToDoApp.to_create_todo(my_list_str)
            cprint ("{} todo list created! \n".format(my_list_str), 'blue')

        except ValueError as e:
            cprint(e, 'red')
    
    @pass_opt
    def do_todo_open(self, arg):
        """
        Finds a task in the todo list and opens it, (prints)
        Usage:
              todo_open <list_param> ["--choice"]
        """
        try:
            open_list = arg["<list_param>"]
            choice = arg["--choice"]
            if open_list_str = " ".join(open_list):
            print (" " + open_list)
            app.ToDoApp.to_open_todo(open_list_str)
            print ("List opened")


            
        except ValueError as e:
            cprint((e), 'red')

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        cprint(('Thankyou for Using this todo Application!'), 'yellow')
        exit()

opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    try:
        ToDoApp().cmdloop()
    except KeyboardInterrupt:
        cprint(('Thankyou for Using This todo application!'), 'yellow')
        exit()
print(opt)