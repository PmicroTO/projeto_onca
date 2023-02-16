def cruder(sql_command):
    import os
    import sqlite3

    dbp = os.path.dirname(os.path.abspath(__file__))
    dbf = os.path.join(dbp, 'biblioteca.db')

    connection = sqlite3.connect(dbf)
    b_cursor = connection.cursor()

    b_cursor.execute(sql_command)

    table = b_cursor.fetchall()

    connection.commit()

    connection.close()
    return table
