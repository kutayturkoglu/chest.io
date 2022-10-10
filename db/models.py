import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='kutay',
    password='pwd123321!',
    auth_plugin='mysql_native_password',
    database='chest'
)

cursor = conn.cursor()

"""
    Create and test database
"""

# cursor.execute("CREATE DATABASE chest")
# cursor.execute("SHOW DATABASES")

# for db in cursor:
#     print(db)

"""
    Create tables
"""

# cursor.execute("""CREATE TABLE User 
#                (user_name VARCHAR(50) NOT NULL UNIQUE, 
#                user_email VARCHAR(50) NOT NULL UNIQUE, 
#                user_pw VARCHAR(50) NOT NULL UNIQUE, 
#                user_id VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE)
#                """)

# cursor.execute("""CREATE TABLE Diary 
#                (diary_date DATE NOT NULL, 
#                user_id VARCHAR(50) NOT NULL, 
#                content VARCHAR(1000) NOT NULL, 
#                diary_id VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE)
#                """)

# cursor.execute("""CREATE TABLE Reminder 
#                (
#                    reminder_header VARCHAR(50) NOT NULL,
#                    user_id VARCHAR(50) NOT NULL,
#                    date_to_be DATETIME NOT NULL,
#                    reminder_id VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE
#                )
#                """)

# cursor.execute("""CREATE TABLE Blog
#                 (
#                     blog_header VARCHAR(50) NOT NULL UNIQUE,
#                     user_id VARCHAR(50) NOT NULL,
#                     blog_content VARCHAR(1000) NOT NULL,
#                     blog_date DATE NOT NULL,
#                     blog_id VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE   
#                 )
#             """)
