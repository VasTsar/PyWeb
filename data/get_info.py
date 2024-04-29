import sqlite3
import random


def get_info():
    con = sqlite3.connect('db/architecture.db')
    cur = con.cursor()
    max_id = cur.execute("""SELECT MAX(id) FROM Objects""").fetchone()[0]
    ids = random.sample(range(1, max_id + 1), 2)
    id1, id2 = int(ids[0]), int(ids[1])
    inf1, img1 = cur.execute("""SELECT information, image FROM Objects
            WHERE id = ?""", (id1,)).fetchall()[0]
    inf2, img2 = cur.execute("""SELECT information, image FROM Objects
            WHERE id = ?""", (id2,)).fetchall()[0]
    return {'id1': id1,
            'id2': id2,
            'img1': img1,
            'img2': img2,
            'inf1': inf1,
            'inf2': inf2
            }
