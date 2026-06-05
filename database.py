import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="blood_bank"
)

cursor = conn.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        blood_group VARCHAR(5),
        contact VARCHAR(15)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blood_stock (
        blood_group VARCHAR(5) PRIMARY KEY,
        units INT DEFAULT 0
    )
    """)

    conn.commit()