import sqlite3

livraria = sqlite3.connect("livraria.db")
livraria.execute("PRAGMA foreign_keys = ON")

c_livraria = livraria.cursor()

print("Connected to the database")

comando_sql = input("Digite seu comando SQL: ")

c_livraria.execute(comando_sql)

livraria.close()
