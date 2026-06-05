import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="blood_bank"
)

cursor = conn.cursor()

print("DONORS")
cursor.execute("SELECT * FROM donors")

for row in cursor.fetchall():
    print(row)

print("\nBLOOD STOCK")
cursor.execute("SELECT * FROM blood_stock")

for row in cursor.fetchall():
    print(row)

conn.close()