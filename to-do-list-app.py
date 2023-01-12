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
    
#This will ask for user inputs to pass information to the database
def addTasktolist():
    TaskName = input("Enter the name of the task: ")
    TaskPriority = input("Enter the priority of the task (1 High 3 Low): ")
    TaskInfo = input("Enter any additional information about the task: ")
    query = """INSERT INTO tasks (TaskName, TaskPriority, TaskInfo) VALUES (?, ?, ?)"""
    try:
        cursor.execute(query, (TaskName, TaskPriority, TaskInfo))
    except sqlite3.IntegrityError:
        print("Task input error")
    else:
        conn.commit()
        print(f"Task {TaskName} added to the list")

#This will flag a task from the taskID Database as completed
def completeTask():
    TaskID = input("Enter the ID of the task you want to complete: ")
    query = """UPDATE tasks SET TasksCompleted = TRUE WHERE taskID = ?"""
    try:
        cursor.execute(query, (TaskID))
    except sqlite3.IntegrityError:
        print("Error with completing this task")
    else:
        conn.commit()
        print(f"Task {TaskID} completed") 