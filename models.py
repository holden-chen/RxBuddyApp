import sqlite3


class Medications:
    """
    class docstring.
    """
    def __init__(self):
        """
        Docstring.
        """
        self.con = sqlite3.connect('medications.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        """
        Docstring.
        """
        # self.cur.execute("""DROP TABLE medications""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS medications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drug_name TEXT,
        side_effects TEXT    
        )""")

    def insert(self, item):
        """
        Docstring.
        """
        self.cur.execute("""INSERT OR IGNORE INTO medications(drug_name, side_effects) VALUES(?, ?)""", item)
        self.con.commit()

    def read(self):
        self.cur.execute("""SELECT * FROM medications""")
        rows = self.cur.fetchall()
        return rows
