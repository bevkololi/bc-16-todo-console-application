import os
from models import *


def to_create_todo(new_list):
	list_data = ToDo(list_name = new_list)
	session.add(list_data)
	session.commit()

#to_create_todo("Create github repo")
#to_create_todo("Update github repo")


def to_open_todo(open_list):
	if type(open_list) == str:
		list_to_get = session.query(ToDo).filter_by(list_name = open_list).first()
	elif type(open_list) == int:
		list_to_get = session.query(ToDo).filter_by(id = open_list).first()
	todo_ref = list_to_get.id
	# print(list_to_get.id)

	add_item = True

	if add_item:
		#will be able to add item in docopt using argument
		new_item = "Push my progress"
		list_item = ToDoItems(item_name = new_item, todo_id = todo_ref)
		session.add(list_item)
		session.commit()


#to_open_todo(4)

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
		print(item.item_name)

#to_view_items(2)

def to_delete_todo(del_list):
	if type(del_list) == str:
		list_to_del = session.query(ToDo).filter_by(list_name = del_list).first()
	elif type(open_list) == int:
		list_to_del = session.query(ToDo).filter_by(id = del_list).first()
	todo_ref = list_to_del.id
to_delete_todo("Create github repo")









