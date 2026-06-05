from database import cursor, conn


def add_donor(name, age, blood_group, contact):
    sql = """
    INSERT INTO donors(name, age, blood_group, contact)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, age, blood_group, contact)

    cursor.execute(sql, values)
    conn.commit()


def view_donors():
    cursor.execute("SELECT * FROM donors")
    return cursor.fetchall()


def search_donor(blood_group):
    cursor.execute(
        "SELECT * FROM donors WHERE blood_group=%s",
        (blood_group,)
    )
    return cursor.fetchall()


def add_blood_stock(group, units):
    cursor.execute("INSERT OR IGNORE INTO blood_stock (blood_group, units) VALUES (?, 0)", (group,))
    cursor.execute("UPDATE blood_stock SET units = units + ? WHERE blood_group=?", (units, group))
    conn.commit()


def request_blood(group, units):
    cursor.execute("SELECT units FROM blood_stock WHERE blood_group=?", (group,))
    result = cursor.fetchone()

    if result and result[0] >= units:
        cursor.execute("UPDATE blood_stock SET units = units - ? WHERE blood_group=?", (units, group))
        conn.commit()
        return True
    return False

def add_blood_stock(group, units):

    cursor.execute(
        "SELECT * FROM blood_stock WHERE blood_group=%s",
        (group,)
    )

    result = cursor.fetchone()

    if result:
        cursor.execute(
            "UPDATE blood_stock SET units=units+%s WHERE blood_group=%s",
            (units, group)
        )
    else:
        cursor.execute(
            "INSERT INTO blood_stock(blood_group, units) VALUES(%s,%s)",
            (group, units)
        )

    conn.commit()

def request_blood(group, units):

    cursor.execute(
        "SELECT units FROM blood_stock WHERE blood_group=%s",
        (group,)
    )

    result = cursor.fetchone()

    if result and result[0] >= units:

        cursor.execute(
            "UPDATE blood_stock SET units=units-%s WHERE blood_group=%s",
            (units, group)
        )

        conn.commit()
        return True

    return False