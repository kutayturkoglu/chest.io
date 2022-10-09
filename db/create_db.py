import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='kutay',
    password='pwd123321!',
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
