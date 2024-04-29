import sqlite3
import random


id1 = int(random.sample(range(1, 4), 1)[0])
id2 = int(random.sample(range(1, 4), 1)[0])
con = sqlite3.connect('db/architecture.db')
cur = con.cursor()
inf1 = cur.execute("""SELECT information FROM Objects
        WHERE id = ?""", (id1,)).fetchone()[0]
inf2 = cur.execute("""SELECT information FROM Objects
        WHERE id = ?""", (id2,)).fetchone()[0]
filenames = ['Narkomfin.jpg', 'Kolomenskoye.jpg', 'Ascension.jpg', 'Simonov.jpg']
img1 = filenames[id1]
img2 = filenames[id2]
