def cruder(sql_command):
    import sqlite3
    connection = sqlite3.connect('./sql_bib/biblioteca.db')
    crsr = connection.cursor()

    crsr.execute(sql_command)

    connection.commit()

    connection.close()
