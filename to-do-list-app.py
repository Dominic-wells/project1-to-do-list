import sqlite3
import os

#This will make a database called "to-do-list"
#If the database already exists, it will connect to it  
db = "to-do-list.db"
conn = sqlite3.connect(db)
cursor = conn.cursor()