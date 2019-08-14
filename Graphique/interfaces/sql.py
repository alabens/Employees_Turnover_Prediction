import sqlite3

conn = sqlite3.connect('PCD.db')
c = conn.cursor()
c.execute("""insert into Entreprise values ('Sofrecom','Sofrecom','sof.kharrat@ensi-uma.tn')""")
