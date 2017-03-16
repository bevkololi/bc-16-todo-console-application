"""
Todo application
Todo list commands
Usage:
    my_to_do todo_create <list_name>
    my_to_do todo_open <list_param> [--choice=name]
    my_to_do item_add <item_name>
    my_to_do list <all_lists>
    my_to_do list_items <all_items> [--choice=name]
    my_to_do del <list_name>
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
from time import sleep
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

os.system('cls')
print("\t****************************************************")
print("\t***  Save tasks to remember, wherever, whenever!  ***")
print("\t*****************************************************")

sleep(4)

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
              todo_open <list_param>... [--choice=name]
        """
        try:
            open_list = arg["<list_param>"]
            choice = arg["--choice"]
            if choice == "name":
                open_list_str = " ".join(open_list)
                print(open_list_str)
            elif choice == "id":
                open_list_str = int(" ".join(open_list))
                print (open_list_str)
            app.ToDoApp.to_open_todo(open_list_str)
            print ("List opened")


            
        except ValueError as e:
            cprint((e), 'red')

    @pass_opt
    def do_add_item(self, arg):
        """
        Adds items in a related todolist.
        Usage:
              item_add <item_name>... 
        """
        try:
            add_item = arg["<item_name>"]
            add_item_str = " ".join(add_item)
            app.ToDoApp.to_add_item(add_item_str, add_item = True)
            


            
        except ValueError as e:
            cprint((e), 'red')

    @pass_opt
    def do_list(self, arg):
        """
        Gives a list of all main todo tasks
        Usage:
              list <all_lists>... 
        
        """
        try:
            cprint ("Here are your todo lists: \n", 'blue')
            app.ToDoApp.to_view_todo()

        except ValueError as e:
            cprint(e, 'red')

    @pass_opt
    def do_list_items(self, arg):
        """
        Finds all items in the todo list
        Usage:
              list_items <all_items>... [--choice=name]
        """
        try:
            cprint ("These are your items: \n", 'blue')
            my_items = arg["<all_items>"]
            choice = arg["--choice"]
            if choice == "name":
                my_items_str = " ".join(my_items)
                print(my_items_str)
            elif choice == "id":
                my_items_str = int(" ".join(my_items))
                print (my_items_str)
            app.ToDoApp.to_view_items(my_items_str)
            


            
        except ValueError as e:
            cprint((e), 'red')


    @pass_opt
    def do_del(self, arg):
        """
        Finds a task in the todo list and deletes it
        Usage:
              del  <list_name>... [--choice=name]
        """
        try:
            del_list = arg["<list_name>"]
            choice = arg["--choice"]
            if choice == "name":
                del_list_str = " ".join(del_list)
                print(del_list_str)
            elif choice == "id":
                del_list_str = int(" ".join(del_list))
                print (del_list_str)
            app.ToDoApp.to_delete_todo(del_list_str)
            print ("List deleted")


            
        except ValueError as e:
            cprint((e), 'red')

    # @pass_opt
    # def do_list_item(self, arg):
    #     """
    #     Adds items in a related todolist.
    #     Usage:
    #           list_item <all_items>... 
        
    #     """
    #     try:
    #         cprint ("Here are your todo items: \n", 'blue')
    #         app.ToDoApp.to_view_items()

    #     except ValueError as e:
    #         cprint(e, 'red')
    
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