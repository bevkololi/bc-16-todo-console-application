import os
from models import *

#import gem
#from gem2 import new_task
# todolist=[]
# todoitems=[]

# def display_title_bar():

# 	#os.system("cls")
# 	print("\t**********************************************")
# 	print("\t***  Hello, This is your to-do list!  *********")
# 	print("\t**********************************************")

				
def to_create_todo(new_list):
	list_data = ToDo(list_name = new_list)
	session.add(list_data)
	session.commit()

to_create_todo("Create github repo")
to_create_todo("Update github repo")


def to_open_todo(open_list):
	if type(open_list) == str:
		list_to_get = session.query(ToDo).filter_by(list_name = open_list).first()
	elif type(open_list) == int:
		list_to_get = session.query(ToDo).filter_by(id = open_list).first()
	todo_ref = list_to_get.id
	# print(list_to_get.id)

	add_item = True

	if add_item:
		new_item = "Push my progress"
		list_item = ToDoItems(item_name = new_item, todo_id = todo_ref)
		session.add(list_item)
		session.commit()


to_open_todo(4)

def to_view_todo():
	all_lists = session.query(ToDo).options(load_only("list_name"))
	for todo in all_lists:
		print (todo.list_name)
to_view_todo()


	
def to_view_items(parent_list):
	if type(parent_list) == str:
		list_to_get = session.query(ToDo).filter_by(list_name = parent_list).first()
		mother_list_id = list_to_get.id
		items_to_get = session.query(ToDoItems).filter_by(todo_id = mother_list_id).options(load_only("item_name"))
	elif type(parent_list) == int:
		items_to_get = session.query(ToDoItems).filter_by(todo_id = parent_list).options(load_only("item_name"))
	for item in items_to_get:
		print(item.name)

to_view_items(2)






# def get_user_choice():
# 	print("\n[1] See my to-do lists.")
# 	print("[2] Add a task in my to-do list.")
# 	print("[4] See my to-do items.")
# 	print("[3] Add an item in my to-do list.")
# 	print("[q] Quit.") 
# 	return input("What would you like to do?") 

# def show_todo_list():
# 	print("\nHere are your to-do lists")
# 	for task in tasks:
# 		print (task.title())1


# def show_todo_items():
# 	print("\nHere are your to-do items")
# 	for item in items:
# 		print (item.title())

# def add_new_task():
# 	new_task=input("\nPlease add your new task.")

# 	if new_task in tasks:
# 		print ("\n%s is already in your to-do list.")
# 	else:
# 		tasks.append(new_task)
# 		print ("You have added %s in your to-do list."%new_task.title())

# def add_new_item():
# 	new_item=input("\nPlease add your new item.")

# 	if new_item in item:
# 		print ("\n%s is already in your to-do item list.")
# 	else:
# 		items.append(new_item)
# 		print ("You have added %s in your to-do item list."%new_item.title())


# #main program
# choice=""
# display_title_bar()
# while choice!="q":
# 	choice=get_user_choice()
# 	display_title_bar()

# 	if choice=="1":
# 		show_todo_list()
# 	elif choice=="2":
# 		add_new_task()
# 	elif choice=="q":
# 		print ("You to-do list has been updated. Bye.")
# 	else:
# 		print("\nI did not understand that choice.\n")