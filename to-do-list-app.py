import sqlite3

#This will make a database called "to-do-list"
#If the database already exists, it will connect to it  
db = "C:/Users/josep/Desktop/project1/to-do-list.db"
conn = sqlite3.connect(db)
cursor = conn.cursor()

#This will create a table in the database
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
    
#This will ask for user inputs to pass information to the database
def addTasktolist():
    TaskName = input("Enter the name of the task: ")
    TaskPriority = input("Enter the priority of the task (1 High 3 Low): ")
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

#This will flag a task from the taskID Database as completed
def completeTask():
    displayAllTasks()
    TaskID = input("Enter the ID of the task you want to complete: ")
    query = """UPDATE tasks SET TasksCompleted = TRUE WHERE taskID = ?"""
    try:
        cursor.execute(query, (TaskID))
    except sqlite3.IntegrityError:
        print("Error with completing this task")
    else:
        conn.commit()
        print(f"Task {TaskID} completed")
        
         
        
 #This will display all the tasks that have not been flagged as completed             
def displayNonCompletedTasks():
    query = """SELECT * FROM tasks WHERE TasksCompleted = 0"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Task that are not yet completed:\n")
    for row in results:
        for item in row:
            print(item, end=" ")
        print("\n")        

#This will display all the tasks that have been added to the database
def displayAllTasks():
    query = """SELECT taskID, TaskName, TaskPriority, TaskInfo, Dateadded, TasksCompleted FROM tasks"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Task that are not yet completed:\n")
    for row in results:
        for item in row:
            print(item, end=" ")
        print("\n")      
        
#This will display all the tasks that have be flagged as completed
def displayAllCompletedTasks():
    query = """SELECT * FROM tasks WHERE TasksCompleted = 1"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Completed Tasks:\n")
    if results == []:
        print("no tasks completed yet, please complete a task first and mark it as completed (option 2)")
    else:
        for row in results:
            for item in row:
                print(item, end=" ")
            print("\n")  
        
#This will delete a completed task from the database.
def deleteCompletedTasks():
    displayAllCompletedTasks()
    TaskID = input("Enter the ID of the task you want delete: ")
    query = """DELETE FROM tasks WHERE TaskID = ?"""
    try:
        cursor.execute(query, (TaskID))
    except sqlite3.IntegrityError:
        print("Error with deleting this task")
    else:
        conn.commit()
        print(f"Task {TaskID} deleted")

#this will delete a tasks from the database
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
        
def oderByPriority():
    query = """SELECT * FROM tasks ORDER BY TaskPriority"""
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows == []:
        print("No tasks added")
    else:
        for row in rows:
            print(row)     

def main():
    makeTable()
    while True:
        print("1. Add a task to the list")
        print("2. Complete a task")
        print("3. Display non completed tasks")
        print("4. Display all completed tasks")
        print("5. Display all tasks")
        print("6. Delete a task")
        print("7. Delete a completed task")
        print("8. Order by priority")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            addTasktolist()
        elif choice == "2":
            completeTask()
        elif choice == "3":    
            displayNonCompletedTasks()
        elif choice == "4":
            displayAllCompletedTasks()
        elif choice == "5":
            displayAllTasks()
        elif choice == "6":
            deleteATask()
        elif choice == "7":
            deleteCompletedTasks()
        elif choice == "8":
            oderByPriority()
        elif choice == "9":   
            print("Goodbye")
            break    
        else:
            print("Invalid choice")
            
            
    
if __name__ == "__main__":
    #This will run the main menu within the 'main' function
    print("\nTo do list app")
    # makeTable()
    main()