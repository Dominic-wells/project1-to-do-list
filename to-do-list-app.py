import sqlite3

#This will make a database called "to-do-list"
#If the database already exists, it will connect to it  
db = "C:/Users/josep/Desktop/project1/to-do-list.db"
conn = sqlite3.connect(db)
cursor = conn.cursor()

#This will create a table in the database if it does not already exist
#Guidenace taken from https://www.sqlitetutorial.net/
def makeTable():
    query ="""CREATE TABLE IF NOT EXISTS tasks
    (taskID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    TaskName TEXT NOT NULL, 
    TaskPriority INTEGER NOT NULL, 
    TaskInfo TEXT NOT NULL,
    Dateadded TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
    TasksCompleted BOOLEAN NOT NULL DEFAULT FALSE)"""
    cursor.execute(query)
    conn.commit()
    
#This will ask users information about the task they they want to add a task to the database 
# they will be asked to enter the name, priority and information about the task they want to add and 
# confirm the task has been added to the database if it has been added successfully
def addTasktolist():
    TaskName = input("Enter the name of the task: ")
    TaskPriority = input("Enter the priority of the task (1=High 3=Low): ")
    TaskInfo = input("Enter any additional information about the task: ")
    query = """INSERT INTO tasks (TaskName, TaskPriority, TaskInfo) VALUES (?, ?, ?)"""
    try:
        cursor.execute(query, (TaskName, TaskPriority, TaskInfo))
    except: 
        print("Task input error")
    else:
        conn.commit()
        print(f"Task {TaskName} added to the list")
        print("\n") 

#This will display all non completed tasks that have been added to the database
#and ask the user to enter the taskID of the task they want to complete
def completeTask():
    displayNonCompletedTasks()
    TaskID = input("Enter the ID of the task you want to complete: ")
    query = """UPDATE tasks SET TasksCompleted = TRUE WHERE taskID = ?"""
    try:
        cursor.execute(query, (TaskID))
    except sqlite3.IntegrityError:
        print("Error with completing this task")
    else:
        conn.commit()
        print(f"Task {TaskID} completed")
        
         
        
 #This will display all the tasks that have not been flagged as completed by the user          
def displayNonCompletedTasks():
    query = """SELECT * FROM tasks WHERE TasksCompleted = 0"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Task that are not yet completed:\n")
    for row in results:
        for item in row:
            print(item, end=" ")
        print("\n")        

#This will display all the tasks that have been added to the database (completed and non completed)
def displayAllTasks():
    query = """SELECT taskID, TaskName, TaskPriority, TaskInfo, Dateadded, TasksCompleted FROM tasks"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Task that are not yet completed:\n")
    if results == []:
        print("no tasks completed yet, please complete a task first and mark it as completed (option 2)")
    else:
        for row in results:
            for item in row:
                print(item, end=" ")
            print("\n")      
        
#This will display all the tasks that have be flagged as completed by the user
def displayAllCompletedTasks():
    query = """SELECT * FROM tasks WHERE TasksCompleted = 1"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Completed Tasks:\n")
    if results == []:
        print("Error with displaying completed tasks(has the task been completed? Did you mark it as completed? Have you tried turning it on or off?)")
    else:
        for row in results:
            for item in row:
                print(item, end=" ")
            print("\n")  
        
#This will delete a completed task from the database once all the completed tasks have been displayed to the user 
# and the user will be asked to enter the taskID of the task they want to delete.
def deleteCompletedTasks():
    displayAllCompletedTasks()
    TaskID = input("Enter the ID of the task you want delete: ")
    query = """DELETE FROM tasks WHERE TaskID = ?"""
    try:
        cursor.execute(query, (TaskID))
    except:
        print("Error with deleting this task")
    else:
        conn.commit()
        print(f"Task {TaskID} deleted")

#this will delete a tasks from the database once all the tasks have been displayed to the user
# and the user will be asked to enter the taskID of the task they want to delete.
def deleteATask():
    displayAllTasks()
    TaskID = input("Enter the ID of the task you want delete: ")
    query = """DELETE FROM tasks WHERE TaskID = ?"""
    try:
        cursor.execute(query, (TaskID))
    except sqlite3.IntegrityError:
        print("Error with deleting this task")
    else:
        conn.commit()
        print(f"Task {TaskID} deleted")
        
#This will display all the non completed tasks that have been added to the database in order of priority with 1 being high and 3 being low.
def orderByPriority():
    query = """SELECT * FROM tasks  WHERE TasksCompleted = 0 ORDER BY TaskPriority"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Completed Tasks:\n")
    if results == []:
        print("Error with displaying tasks by priority")
    else:
        for row in results:
            for item in row:
                print(item, end=" ")
            print("\n")  
    
#This will edit a task from the database once non completed tasks have been displayed to the user, 
# user will be asked to enter the taskID of the task they want to edit, 
# then the user will be asked to enter the new name, priority and information about the task
def editTask():
    displayNonCompletedTasks()
    taskID = input("Enter the ID of the task you want to edit: ")
    taskName = input("Enter the new name of the task: ")
    taskPriority = input("Enter the new priority of the task(1=High 3=Low): ")
    taskInfo = input("Enter the new information about the task: ")
    query = """UPDATE tasks SET TaskName = ?, TaskPriority = ?, TaskInfo = ? WHERE taskID = ?"""
    try:
        cursor.execute(query, (taskName, taskPriority, taskInfo, taskID))
    except:
        print("Error with editing this task")
    else:
        conn.commit()
        print(f"Task {taskID} edited")        
        
        
#This will display a menu to the user and ask them to enter their choice by entering a number.
# This will then call the function that the user has chosen. if the user enters a number that is not in the menu an invalid choice message will be displayed. 
# Users can exit the program by entering 10 in the menu, A goodbye message will be displayed to the user when they exit the program.
def main():
    makeTable()
    while True:
        print("1. Add a task to the list")
        print("2. Complete a task")
        print("3. Edit a task")
        print("4. Display non completed tasks")
        print("5. Display all completed tasks")
        print("6. Display all tasks")
        print("7. Delete a task")
        print("8. Delete a completed task")
        print("9. Order tasks by priority")
        print("10. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            addTasktolist()
        elif choice == "2":
            completeTask()
        elif choice == "3":
            editTask()
        elif choice == "4":
            displayNonCompletedTasks()
        elif choice == "5":
            displayAllCompletedTasks()
        elif choice == "6":
            displayAllTasks()
        elif choice == "7":
            deleteATask()
        elif choice == "8":
            deleteCompletedTasks()
        elif choice == "9":
            orderByPriority()
        elif choice == "10":
            print ("Goodbye,See you next time")
            break
        else:
            print("Invalid choice")                        
      
#This will call the main function when the program is run
if __name__ == "__main__":
    print("\nTo do list app")
    main()