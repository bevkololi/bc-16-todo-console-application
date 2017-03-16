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
conn=sqlite3.connect('todolists.db')
c1=conn.cursor()
conn2=sqlite3.connect('todolists.db')
c2=conn2.cursor()


Base = declarative_base()

class ToDo(Base):  #<------------------------- 
    __tablename__  = "todolists"    
    id             = Column(Integer, primary_key=True) 
    list_name      = Column(String(50))                                    
    done           = Column(Boolean,default=False)               
         # defaults can be specified as functions
    

class ToDoItems(Base): 
    __tablename__  = "todoitems"    
    id             = Column(Integer,primary_key=True) 
    item_name      = Column(String(50))                                    
    done           = Column(Boolean,default=False)
    todo_id        = Column(Integer,ForeignKey('todolists.id')) 
    todo           = relationship("ToDo",backref="todolists")                
           
    

Base.metadata.create_all(engine)
