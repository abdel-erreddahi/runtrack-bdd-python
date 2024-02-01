import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='laplateforme'
)


cursor = conn.cursor()

cursor.execute("SELECT capacite  FROM salle;")


results = cursor.fetchall()

superficieTotal = 0
for row in results:
    superficieTotal = superficieTotal + row[0]
print('La capacite de toutes les salles est de :', superficieTotal)


cursor.close()
conn.close()
