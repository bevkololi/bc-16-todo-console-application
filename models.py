from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import load_only
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Sequence,
    create_engine,
    Float,
    )
import datetime
import os
import sqlite3
engine = create_engine('sqlite:///todolists.db', echo=False)

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

#DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class ToDo(Base):  #<------------------------- 
    __tablename__  = "todolists"    #matches the name of the actual database table
    id             = Column(Integer, primary_key=True) # plays nice with all major database engines
    list_name      = Column(String(50))                                    # string column need lengths
    done           = Column(Boolean,default=False)               # assumes there is a table in the database called 'authors' that has an 'id' column
         # defaults can be specified as functions
    

class ToDoItems(Base):  #<------------------------- B
    __tablename__  = "todoitems"    #matches the name of the actual database table
    id             = Column(Integer,primary_key=True) # plays nice with all major database engines
    item_name      = Column(String(50))                                    # string column need lengths
    done           = Column(Boolean,default=False)
    todo_id        = Column(Integer,ForeignKey('todolists.id')) 
    todo           = relationship("ToDo",backref="todolists")                # assumes there is a table in the database called 'authors' that has an 'id' column
           # defaults can be specified as functions
    

Base.metadata.create_all(engine)
# #fetch everything
# lBooks = DBSession.query(Book)  #returns a Query object. 
# for oBook in lBooks:
#     print oBook.name 