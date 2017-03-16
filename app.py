import os
from models import *

class ToDoApp():


	def to_create_todo(new_list):
		list_data = ToDo(list_name = new_list)
		session.add(list_data)
		session.commit()

	# to_create_todo("Create github repo")
	# to_create_todo("Update github repo")

	todo_ref = 0
	def to_open_todo(open_list):
		if type(open_list) == str:
			list_to_get = session.query(ToDo).filter_by(list_name = open_list).first()
		elif type(open_list) == int:
			list_to_get = session.query(ToDo).filter_by(id = open_list).first()
		print("Successfully opened " + list_to_get.list_name)
		global todo_ref
		todo_ref = list_to_get.id

	def to_add_item(new_item, add_item = False):
		if add_item:
			#will be able to add item in docopt using argument
			list_item = ToDoItems(item_name = new_item, todo_id = todo_ref)
			session.add(list_item)
			session.commit()
			print("Item Added Successfully!")
	


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
			list_to_del = session.query(ToDo).filter_by(list_name = del_list).first()
		elif type(del_list) == int:
			list_to_del = session.query(ToDo).filter_by(id = del_list).first()
		session.delete(del_list)
		session.commit()

	#to_delete_todo(0)
			
			

		
	# to_delete_todo()

	# def to_delete_items():
	# 	del_item = session.query(ToDoItems).options(load_only("item_name"))
	# 	session.delete(del_item)
	# 	session.commit()
			
	


# def to_view_done_tasks():
# 	items_to_get = session.query(ToDoItems).filter_by(todo_id = mother_list_id).options(load_only("item_name"))
# 	done = False
# 	for items in items_to_get:
# 		complete = input("Have you completed this task [yN]?").lower().strip()
# 		if complete == "y":
# 			return True
# to_view_done_tasks()
	 	
	 		





