import sqlite3
import os

#This will make a database called "to-do-list"
#If the database already exists, it will connect to it  
db = "to-do-list.db"
conn = sqlite3.connect(db)
cursor = conn.cursor()

#This will create a table in the database
#Guidenace taken from https://www.sqlitetutorial.net/
def makeTable():
    query ="""CREATE TABLE tasks
     (taskID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    TaskName TEXT NOT NULL, 
    TaskPriority INTEGER NOT NULL, 
    TaskInfo TEXT NOT NULL,
    Dateadded TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
    TasksCompleted BOOLEAN NOT NULL DEFAULT FALSE)"""
    cursor.execute(query)
    conn.commit()
