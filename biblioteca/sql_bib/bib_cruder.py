def cruder(sql_command):
    import sqlite3
    connection = sqlite3.connect('./sql_bib/biblioteca.db')
    b_cursor = connection.cursor()

    b_cursor.execute(sql_command)

    table = b_cursor.fetchall()

    connection.commit()

    connection.close()

    return table
