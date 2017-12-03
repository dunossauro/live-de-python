"""
DDL - Manipulação da tabela
"""
import sqlite3

con = sqlite3.connect('base.db')

cur = con.cursor()

sql = """
CREATE TABLE carros (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)"""

cur.execute(sql)
con.commit()
con.close()
