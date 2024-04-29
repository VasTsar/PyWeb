import sqlite3
import random


ids = random.sample(range(1, 4), 2)
id1, id2 = int(ids[0]), int(ids[1])
con = sqlite3.connect('db/architecture.db')
cur = con.cursor()
inf1 = cur.execute("""SELECT information FROM Objects
        WHERE id = ?""", (id1,)).fetchone()[0]
inf2 = cur.execute("""SELECT information FROM Objects
        WHERE id = ?""", (id2,)).fetchone()[0]
filenames = ['Narkomfin.jpg', 'Kolomenskoye.jpg', 'Ascension.jpg', 'Simonov.jpg']
img1, img2 = filenames[id1 - 1], filenames[id2 - 1]
