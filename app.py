import os
from models import *
from tabulate import tabulate
from termcolor import cprint, colored



class ToDoApp():


	def to_create_todo(new_list):
		check_list = session.query(ToDo).filter_by(list_name = new_list).first()
		if check_list:
			cprint("Oops, this todo list already exists!", 'red')
		else:
			list_data = ToDo(list_name = new_list)
			session.add(list_data)
			session.commit()
			cprint ("{} todo list created! \n".format(new_list), 'green')
		




	# to_create_todo("Update github repo")

	todo_ref = 0
	def to_open_todo(open_list):
		if type(open_list) == str:
			list_to_get = session.query(ToDo).filter_by(list_name = open_list).first()
			if list_to_get:
				cprint(("Successfully opened " + list_to_get.list_name), 'green')
			else:
				cprint("This list does not exist!", 'red')
		elif type(open_list) == int:
			list_to_get = session.query(ToDo).filter_by(id = open_list).first()
			if list_to_get:
				print("Successfully opened " + list_to_get.list_name)
			else:
				print("This list does not exist!")
		global todo_ref
		todo_ref = list_to_get.id

	def to_add_item(new_item, add_item = False):
		if add_item:
			#will be able to add item in docopt using argument
			list_item = ToDoItems(item_name = new_item, todo_id = todo_ref)
			session.add(list_item)
			session.commit()
			print("Item Added Successfully!")
	# def to_add_item(new_item, add_item = False):
	# 	if add_item:
	# 		#will be able to add item in docopt using argument
	# 		list_item = ToDoItems(item_name = new_item, todo_id = todo_ref)
	# 		session.add(list_item)
	# 		session.commit()
	# 		print("Item Added Successfully!")

	
	


	# to_open_todo()

	def to_view_todo():
		all_lists = session.query(ToDo).options(load_only("list_name"))
		for todo in all_lists:
			print (todo.list_name)
	# to_view_todo()





	def to_view_items(parent_list):
		if type(parent_list) == str:
			list_to_get = session.query(ToDo).filter_by(list_name = parent_list).first()
			mother_list_id = list_to_get.id
			items_to_get = session.query(ToDoItems).filter_by(todo_id = mother_list_id).options(load_only("item_name"))
		elif type(parent_list) == int:
			items_to_get = session.query(ToDoItems).filter_by(todo_id = parent_list).options(load_only("item_name"))
		for item in items_to_get:
			print(item.item_name)

	to_view_items(3)

	def to_delete_todo(del_list):
		if type(del_list) == str:
			list_to_del = session.query(ToDo).filter_by(list_name = del_list).options(load_only("list_name"))
		elif type(del_list) == int:
			list_to_del = session.query(ToDo).filter_by(id = del_list).options(load_only("list_name"))
		for deleted in list_to_del:
			print(deleted.list_name)
		list_to_del.delete()
		session.commit()

	def to_delete_item(del_item):
		if type(del_item) == str:
			item_to_del = session.query(ToDoItems).filter_by(item_name = del_item).options(load_only("item_name"))
		elif type(del_item) == int:
			item_to_del = session.query(ToDoItems).filter_by(id = del_item).options(load_only("item_name"))
		for deleted in item_to_del:
			print(deleted.item_name)
		item_to_del.delete()
		session.commit()


			
	



	 		





