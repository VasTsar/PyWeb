import sqlite3
import random


ids = random.sample(range(1, 4), 2)
id1, id2 = int(ids[0]), int(ids[1])
con = sqlite3.connect('db/architecture.db')
cur = con.cursor()
inf1, img1 = cur.execute("""SELECT information, image FROM Objects
        WHERE id = ?""", (id1,)).fetchall()[0]
inf2, img2 = cur.execute("""SELECT information, image FROM Objects
        WHERE id = ?""", (id2,)).fetchall()[0]
